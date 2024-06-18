# N:M chatting

import socketserver     # TCPServer, ThreadingMixIn
import threading

group_queue = []

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        # Show a client connection information
        print("> client connected by IP address {0} with Port number {1}".format(self.client_address[0], self.client_address[1]))
        global group_queue
        group_queue.append(self.request)

        while True:
            recvData = self.request.recv(1024)
            if not recvData or recvData.decode("utf-8") == "quit":
                group_queue.remove(self.request)
                break
            else:
                print("> received (", recvData.decode("utf-8"), ") and echoed to ", len(group_queue), 'clients')
                for conn in group_queue:
                    conn.sendall(recvData)

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