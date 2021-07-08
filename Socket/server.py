import socket

print("SERVER START")
PORT = 65432
host = socket.gethostname()
print(host)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,PORT))
    s.listen()
    conn,addr = s.accept()
    print("CONNECTION-----",conn)
    print("ADDRESS-----",addr)

    with conn:
        print("Connected by",addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data)