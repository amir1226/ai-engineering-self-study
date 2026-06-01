from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, ToolMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from typing import Annotated, Iterator, Sequence, TypedDict

load_dotenv()



class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    
@tool
def add(a: int, b: int):
    """ Addition function that adds 2 number together"""
    return a+b

@tool
def substract(a: int, b: int):
    """ Addition function that substract 2 number together"""
    return a-b

@tool
def multiply(a: int, b: int):
    """ Addition function that mupltiply 2 number together"""
    return a*b

tools = [add, substract, multiply]

model = ChatOpenAI(
    model="gpt-5.4-mini", 
    use_responses_api=True
).bind_tools(tools)

def model_Call(state: AgentState) -> AgentState:
    """This node will solve the request you input"""
    system_prompt = SystemMessage(
        content="You are my AI assistant, please answer my query to the best of your ability."
    )
    response = model.invoke([system_prompt] + state["messages"])
    return {"messages": [response]}

def should_continue(state: AgentState) -> AgentState:
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return "end"
    else:
        return "continue"


graph = StateGraph(AgentState)
graph.add_node("the_agent", model_Call)
graph.set_entry_point("the_agent")

tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

graph.add_conditional_edges(
    "the_agent",
    should_continue,
    {
        "continue": "tools",
        "end": END
    }
)

graph.add_edge("tools", "the_agent")

app = graph.compile()

def print_stream(stream: Iterator):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()
            
if __name__ == "__main__":
    inputs = {"messages": [("user", "Add 39 + 11 and then multiply the result by 5")]}
    print_stream(app.stream(inputs, stream_mode="values"))