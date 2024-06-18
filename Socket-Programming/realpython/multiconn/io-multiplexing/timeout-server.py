# from. https://itholic.github.io/python-select/
"""
timeout은 비효율적
ex. 소켓 10개 순환 
    -> 1 지나고 1에 client가 요청하면 처리하는 다른 client가 없어도 10초 대기가 필요
"""

import socket

IP = ''
PORT1 = 5050
PORT2 = 5060
SIZE = 1024
ADDR1 = (IP, PORT1)
ADDR2 = (IP, PORT2)

# 서버 소켓1 설정
server_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket1.settimeout(1)
server_socket1.bind(ADDR1)  # 주소 바인딩
server_socket1.listen()

# 서버 소켓2
server_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket2.settimeout(1)
server_socket2.bind(ADDR2)
server_socket2.listen()


# inf loop
# client 접속이 없어도 무한으로 돌며 서버가 소켓 처리
while True:
    try:
        print('hello socket1')
        client_socket, cliend_addr = server_socket1.accept()  # 수신 대기
        msg = client_socket.recv(SIZE)  # client 메세지 반환
        print("[{}] message : {}".format(cliend_addr, msg))

        client_socket.sendall('welcome 5050!'.encode())  # client 응답
        client_socket.close()       # with 쓰면 필요없음
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except socket.timeout:
        pass

    try:
        print('hello socket2')
        client_socket, cliend_addr = server_socket2.accept()  # 수신 대기
        msg = client_socket.recv(SIZE)  # client 메세지 반환
        print("[{}] message : {}".format(cliend_addr, msg))

        client_socket.sendall('welcome 5050!'.encode())  # client 응답
        client_socket.close()       # with 쓰면 필요없음
    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except socket.timeout:
        pass

