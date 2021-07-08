import socket

host = socket.gethostname()
print(host)
PORT = 65432     # The port used by the server

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host,PORT))

    #s.send("Hello Python".encode())
    s.send(b"Hello Python")

    data = s.recv(1024).decode()

print("Received",data)