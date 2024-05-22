import socketserver     # TCPServer, ThreadingMixIn
import threading

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        # Show a client connection information
        print("> client connected by IP address {0} with Port number {1}".format(self.client_address[0], self.client_address[1]))

        while True:
            recvData = self.request.recv(1024)
            cur_thread = threading.current_thread()
            print("> echoed: ", recvData.decode("utf-8"), "by", cur_thread)
            self.request.sendall(recvData)          # self.request == clientSocket
            if not recvData or recvData.decode("utf-8") == "quit":
                break

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 65432
    print("> echo-server is activated")

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    with server:
        ip, port = server.server_address

        server_thread = threading.Thread(target=server.serve_forever)

        server_thread.daemon = True
        server_thread.start()
        print("> server loop running in thread (main thread): ", server_thread.name)

        baseThreadNumber = threading.active_count()
        while True:
            msg = input("> ")
            if not msg or msg == "quit":
                if baseThreadNumber == threading.active_count():
                    print("> stop procedure started")
                    break
                else:
                    print("> active threads are remained: ", threading.active_count())
        
        print("> echo-server is de-activated")
        server.shutdown()