import socket

PORT = 50000    # port to listen on(non-privileged ports are > 1023)
host = socket.gethostname()

server_socket = socket.socket()
server_socket.bind((host,PORT))
print("SERVER START")
server_socket.listen(2)

conn, addr = server_socket.accept()
print("Connection from:" + str(addr))

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("from connected user:" + str(data))
    data = input("->")
    conn.send(data.encode())

conn.close()

if __name__ == "__main__":
    server_program()