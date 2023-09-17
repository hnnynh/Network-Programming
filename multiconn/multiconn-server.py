# listening socket으로 대기열 생성

import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)     # put socket in non-blocking mode
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE       # ready for reading and writing
    sel.register(conn, events, data=data)


# How a client connection is handled when it's ready
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:     # True when the socket is ready for reading
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data      # can be sent later
        else:       # == client ahs closed their socket (client가 빈 body 소켓 보내면 연결 종료)
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:    # True when the socket is ready for writing
        if data.outb:
            print(f"Echoing {data.outb!r} to {data.addr}")
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]        # bytes sent are removed from the send buffer


if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <host> <port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print(f"Listening on {(host, port)}")
lsock.setblocking(False)        # call it to configure the socket in non-blocking mode
sel.register(lsock, selectors.EVENT_READ, data=None)    # registers socket to be monitored with sel.select() for the events

# event loop
try:
    while True:
        events = sel.select(timeout=None)   # sockets ready for I/O
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()


"""
fileobj is the socket object, 
 and mask is an event mask of the operations that are ready.

If key.data is None, 
 then you know it’s from the listening socket and you need to accept the connection. 
You’ll call your own accept_wrapper() function to get the new socket object and register it with the selector. 
You’ll look at that in a moment.

If key.data is not None, 
 then you know it’s a client socket that’s already been accepted, and you need to service it. 
service_connection() is then called with key and mask as arguments, and that’s everything you need to operate on the socket.
"""