import socket

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(("0.0.0.0",9999))
        msg = client.recv(1024)
        print("server says:", msg.decode())
except ConnectionRefusedError:
    print(f"Could not connect to server at 0.0.0.0:9999")
except Exception as e:
    print(f"An error occurred: {e}")
