import socket
import threading
import queue

messages = queue.Queue()
clients = []

# AF_INET: IPv4, SOCK_DGRAM: UDP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 65432))

server.settimeout(1)

running = True

def receive():
    while running:
        try:
            message, client = server.recvfrom(1024)
            # print(f"Received message from {client}: {message.decode()}")
            messages.put((message, client))
        except socket.timeout:
            continue
        except Exception as e:
            #print(f"Error receiving message: {e}")
            pass
            
def broadcast():
    while running:
        while not messages.empty():
            message, sender = messages.get()
            # print(f"Broadcasting message from {sender}: {message.decode()}")
            if sender not in clients:
                clients.append(sender)
            for client in clients:
                try:
                    if message.decode().startswith("JOIN:"):
                        name = message.decode()[message.decode().find(":")+1:]
                        server.sendto(f"{name} has joined the chat.".encode(), client)
                    else:
                        server.sendto(message, client)
                except Exception as e:
                    # print(f"Error broadcasting message to {client}: {e}")
                    clients.remove(client)

if __name__ == "__main__":
    print("UDP server is listening...")
    receive_thread = threading.Thread(target=receive, daemon=True)
    broadcast_thread = threading.Thread(target=broadcast, daemon=True)
    receive_thread.start()
    broadcast_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Server is shutting down...")
        running = False
        server.close()