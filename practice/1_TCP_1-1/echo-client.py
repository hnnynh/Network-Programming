import socket

# Server addr & port
HOST = "127.0.0.1"
PORT = 65432

print("> echo-client is activated")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientS:
    clientS.connect((HOST, PORT))
    while True:
        sendMsg = input("> ")
        clientS.sendall(bytes(sendMsg, "utf-8"))
        recvData = clientS.recv(1024)
        print("> received: ", recvData.decode("utf-8"))
        if sendMsg == "quit":
            break

print("> echo-client is de-activated")