import socket
import threading

# Server addr & port
HOST = "127.0.0.1"
PORT = 65432

def recvHandler(clientS):
    while True:
        recvData = clientS.recv(1024)
        print("> received: ", recvData.decode("utf-8"))
        if not recvData or recvData.decode("utf-8") == "quit":
            break

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as clientS:     
        clientThread = threading.Thread(target=recvHandler, args=(clientS,))
        clientThread.daemon = True
        clientThread.start()

        while True:
            sendMsg = input("> ")
            clientS.sendto(bytes(sendMsg, "utf-8"), (HOST, PORT))
            if sendMsg == "quit":
                break
        

if __name__ == "__main__":
    print("> echo-client is activated")
    main()
    print("> echo-client is de-activated")