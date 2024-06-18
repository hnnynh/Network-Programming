import socketserver

group_queue = []

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        recvData = self.request[0].strip()
        recvSocket = self.request[1]

        recvCmd = recvData.decode("utf-8")
        if recvCmd[0] == "#" or recvCmd == "quit":
            if recvCmd == "#REG":
                print("> client registered", self.client_address)
                group_queue.append(self.client_address)
            elif recvCmd == "#DEREG" or recvCmd == "quit":
                if group_queue.__contains__(self.client_address) == True:
                    print("> client de-registered", self.client_address)
                    group_queue.remove(self.client_address)

        else:
            if len(group_queue) == 0:
                print("> no clinets to echo")
            elif group_queue.__contains__(self.client_address) == False:
                print("> ignores a message from un-registered client")
            else:
                print("> received (", recvData.decode("utf-8"), ") and echoed to ", len(group_queue), "clients")
                for clientConn in group_queue:
                    recvSocket.sendto(recvData, clientConn)

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 65432
    print("> echo-server is activated")
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()
    print("> echo-server is de-activated")
                      