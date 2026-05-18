import threading
import socket

host = '127.0.0.1'
port = 65432
# AF_INET: IPv4, SOCK_STREAM: TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

running = True
server.settimeout(1)

def broadcast(message):
    dead_clients = []

    for client in clients:
        try:
            client.send(message)

        except:
            dead_clients.append(client)

    for client in dead_clients:
        if client in clients:
            clients.remove(client)

def handle(client):
    global running

    while running:
        try:
            message = client.recv(1024)

            if not message:
                break

            broadcast(message)

        except Exception:
            break

    if client in clients:
        index = clients.index(client)

        clients.remove(client)
        client.close()

        nickname = nicknames[index]
        nicknames.remove(nickname)

        broadcast(f'{nickname} left the chat!'.encode())

def receive():
    while running:
        try:
            client, address = server.accept()

            print(f'Connected with {address}')

            client.send(b'HI')

            nickname = client.recv(1024).decode()

            nicknames.append(nickname)
            clients.append(client)

            broadcast(f'{nickname} joined the chat!'.encode())

            thread = threading.Thread(
                target=handle,
                args=(client,),
                daemon=True
            )

            thread.start()

        except socket.timeout:
            continue

if __name__ == "__main__":
    print('Server is listening...')

    try:
        receive()

    except KeyboardInterrupt:
        print("\nShutting down server...")

    running = False

    for client in clients:
        client.close()

    server.close()