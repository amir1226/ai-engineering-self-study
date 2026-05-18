import socket
import threading
import random

# AF_INET: IPv4, SOCK_DGRAM: UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("localhost", random.randint(8001, 9000)))
client.settimeout(1)

name = input("Enter your name: ")

running = True

def receive():
    while running:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
            
        except socket.timeout:
            continue
        except Exception as e:
            print(f"Error receiving message: {e}")

if __name__ == "__main__":
    receive_thread = threading.Thread(target=receive,daemon=True)

    receive_thread.start()

    client.sendto(f"JOIN:{name}".encode(),("localhost", 65432))

    try:
        while True:
            message = input()

            if message.lower() == "exit":
                break

            client.sendto(
                f"{name}: {message}".encode(),
                ("localhost", 65432)
            )

    except KeyboardInterrupt:
        # Ensure graceful shutdown on Ctrl+C or similar interrupts
        pass
    finally:
        print("Closing client...")
        running = False
        client.close()