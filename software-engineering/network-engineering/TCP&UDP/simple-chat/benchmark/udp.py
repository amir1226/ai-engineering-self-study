import socket
import time
import statistics

HOST = "127.0.0.1"
PORT = 65432

NUM_REQUESTS = 1_000
PAYLOAD = b"ping"

latencies = []
lost_packets = 0

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.settimeout(1)

print("Running UDP latency benchmark...")

for _ in range(NUM_REQUESTS):

    try:
        start = time.perf_counter_ns()

        client.sendto(PAYLOAD, (HOST, PORT))

        response, _ = client.recvfrom(1024)

        end = time.perf_counter_ns()

        rtt_ms = (end - start) / 1_000_000

        latencies.append(rtt_ms)

    except socket.timeout:
        lost_packets += 1

client.close()

latencies.sort()

p50 = latencies[int(len(latencies) * 0.50)]
p90 = latencies[int(len(latencies) * 0.90)]
p99 = latencies[int(len(latencies) * 0.99)]

print("\nUDP RESULTS")
print(f"Requests: {NUM_REQUESTS}")
print(f"Successful: {len(latencies)}")
print(f"Lost packets: {lost_packets}")
print(f"Packet loss: {(lost_packets / NUM_REQUESTS) * 100:.2f}%")

print(f"Average RTT: {statistics.mean(latencies):.4f} ms")
print(f"P50 RTT: {p50:.4f} ms")
print(f"P90 RTT: {p90:.4f} ms")
print(f"P99 RTT: {p99:.4f} ms")
print(f"Min RTT: {min(latencies):.4f} ms")
print(f"Max RTT: {max(latencies):.4f} ms")