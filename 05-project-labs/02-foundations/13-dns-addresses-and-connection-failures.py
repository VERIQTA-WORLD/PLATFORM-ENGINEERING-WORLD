import socket
addresses = socket.getaddrinfo("localhost", 18081, type=socket.SOCK_STREAM)
print("loopback results", len(addresses) > 0)
print("IPv4 loopback", socket.inet_aton("127.0.0.1").hex())
try:
    with socket.create_connection(("127.0.0.1", 18089), timeout=1):
        print("unexpected listener on test port")
except OSError:
    print("unused test port is not reachable")
