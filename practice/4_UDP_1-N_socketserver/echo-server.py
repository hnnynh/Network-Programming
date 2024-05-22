import socketserver
# Single thread

class MyUDPHandler(socketserver.BaseRequestHandler):
    # UDP - Connectionless
    
    def handle(self):
        recvData = self.request[0].strip()
        recvSocket = self.request[1]
        print("> echoed: ", recvData.decode("utf-8"))
        recvSocket.sendto(recvData, self.client_address)

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 65432
    print("> echo-server is activated")

    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()
        
    print("> echo-server is de-activated")