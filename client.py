import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1234))

while True:
    client.send(input("B :").encode("utf-8"))
    msg = client.recv(1024).decode("utf-8")
    if msg.lower() == 'quit':
        break
    else :
        print("A :", msg)

client.close()

# try:
#     while True:
#         message = input("message : ")
#         if message.lower() == 'quit':
#             break
#         client.send(message.encode())
#         response = client.recv(1024).decode()
#         print("response:", response)
# finally:
#     client.close()
