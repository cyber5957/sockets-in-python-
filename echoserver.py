import socket

HOST = "0.0.0.0"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"Listening on {HOST}:{PORT}")

try:
    while True:
        client, addr = server.accept()
        print(f"Accepted connection from {addr}")
        with client:
            client.send(b"hello from the server\n")
except KeyboardInterrupt:
    print("\nServer shutting down.")
finally:
    server.close()