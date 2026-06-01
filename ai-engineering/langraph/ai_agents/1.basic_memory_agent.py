from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]

llm = ChatOpenAI(
    model="gpt-5.5", 
    use_responses_api=True, 
    reasoning_effort=None
)

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    content = response.content
    if isinstance(content, list):
        texts = [b["text"] for b in content if isinstance(b, dict) and "text" in b]
        text = " ".join(texts) if texts else str(content)
    else:
        text = content
    print(f"\nAI: {text}")
    return {"messages": state["messages"] + [response]}


graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile()

messages = []
user_input = input("User: ")
while user_input != "exit":
    messages.append(HumanMessage(content=user_input))
    result = agent.invoke(AgentState(messages=messages))
    messages = result["messages"]
    user_input = input("User: ")