import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1234))
server.listen(5)
print("server started")
client, addr = server.accept()
print(f"connect to {addr}")

while True:
    msg = client.recv(1024).decode("utf-8")
    if msg.lower() == 'quit':
        break
    else :
        print("B :", msg)
    
    client.send(input("A :").encode("utf-8"))

client.close()
server.close()

    # try:
    #     while True:
    #         data = client.recv(1024)
    #         if not data:
    #             break
    #         print("from client:", data.decode())
    #         client.send("msg received".encode())
    # finally:
    #     client.close()
    #     print(f"connection closed from {addr}")
    #     break
