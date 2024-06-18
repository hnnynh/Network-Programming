import socket

HOST = "127.0.0.1"
PORT = 65432  

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverS:
        try: 
            if serverS.bind((HOST, PORT)) == -1:
                print("> bind() failed and program terminated")
                serverS.close()
                return
        except Exception as exceptionObj:
            print("> bind() failed by exception: ", exceptionObj)
            serverS.close()
            return
        
        if serverS.listen() == -1:
            print("> listen() failed and program terminated")
            serverS.close()
            return
        
        clientS, clientAddr = serverS.accept()

        with clientS:
            print("> client connected by IP address {0} with Port number {1}".format(clientAddr[0], clientAddr[1]))
            while True:
                recvData = clientS.recv(1024)
                print("> echoed: ", recvData.decode("utf-8"))
                clientS.sendall(recvData)
                if not recvData or recvData.decode("utf-8") == "quit":
                    break


if __name__ == "__main__":
    print("> echo-server is activated")
    main()
    print("> echo-server is de-activated")