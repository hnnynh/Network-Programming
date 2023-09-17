# echo-server.py
# Single Connection

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# with -> 자동 close
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()     # accept 블로킹
    with conn:      
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

"""
listening socket 하나에 대기열 생성
-> accept() 될 때마다 각자 established socket 하나씩

listening socket 여러개를 두고 timeout을 거는 등의 방법으로 여러 소켓 소화 가능
"""