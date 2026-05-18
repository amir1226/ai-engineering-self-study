import socket
import threading

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 65432))

running = True

def receive():
    global running

    while running:
        try:
            message = client.recv(1024)

            # servidor desconectado
            if not message:
                print("Server disconnected.")
                break

            decoded = message.decode('ascii')

            if decoded == 'HI':
                client.send(nickname.encode('ascii'))
            else:
                print(decoded)

        except Exception as e:
            if running:
                print(f"Receive error: {e}")
            break

    running = False

def write():
    global running

    while running:
        try:
            text = input()

            if text.lower() == "exit":
                break

            message = f"{nickname}: {text}"

            client.send(message.encode('ascii'))

        except Exception as e:
            if running:
                print(f"Write error: {e}")
            break

    running = False

if __name__ == "__main__":

    receive_thread = threading.Thread(
        target=receive,
        daemon=True
    )

    write_thread = threading.Thread(
        target=write,
        daemon=True
    )

    receive_thread.start()
    write_thread.start()

    try:
        while running:
            pass

    except KeyboardInterrupt:
        print("\nClosing client...")

    running = False
    client.close()