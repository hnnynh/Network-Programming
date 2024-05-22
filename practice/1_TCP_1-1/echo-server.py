import socket

HOST = "127.0.0.1"
PORT = 65432  

print("> echo-server is activated")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverS:
    serverS.bind((HOST, PORT))
    serverS.listen()
    clientS, clientAddr = serverS.accept()
    with clientS:      
        print("> client connected by IP address {0} with Port number {1}".format(clientAddr[0], clientAddr[1]))
        while True:
            recvData = clientS.recv(1024)
            print("> echoed: ", recvData.decode("utf-8"))
            clientS.sendall(recvData)
            if not recvData or recvData.decode("utf-8") == "quit":
                break
            
print("> echo-server is de-activated")