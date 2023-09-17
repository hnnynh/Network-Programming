# from. https://itholic.github.io/python-select/
"""
.select() - 비동기 I/O 
    -> 동기적인 입출력은 event loop를 사용자가 정의

1. 다중 소켓 모니터링
2. 블로킹 + 비블로킹 가능
3. 네크워크 또는 파일 I/O 비동기적 처리 
    -> 동시에 여러 작업 처리 및 I/O 대기 시간 최소화
"""


import socket
import select

IP = ''
PORT1 = 5050
PORT2 = 5060
SIZE = 1024
ADDR1 = (IP, PORT1)
ADDR2 = (IP, PORT2)

# 서버 소켓1 설정
server_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket1.bind(ADDR1)  # 주소 바인딩
server_socket1.listen()

# 서버 소켓2
server_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket2.bind(ADDR2)
server_socket2.listen()

# 접속 대기할 소켓 리스트
read_socket_list = [server_socket1, server_socket2]

# inf loop
while True:
    # select 선언 - 접속 대기 중인 소켓 리스트 conn_read_socket_list
    conn_read_socket_list, conn_write_socket_list, conn_except_socket_list = select.select(read_socket_list, [], [])
    for conn_read_socket in conn_read_socket_list:
        if conn_read_socket == server_socket1:
            print('hello socket1')
            client_socket, cliend_addr = server_socket1.accept()  # 수신 대기
            msg = client_socket.recv(SIZE)  # client 메세지 반환
            print("[{}] message : {}".format(cliend_addr, msg))

            client_socket.sendall('welcome 5050!'.encode())  # client 응답
            client_socket.close()       # 클라이언트 소켓 종료

        elif conn_read_socket == server_socket2:
            print('hello socket2')
            client_socket, cliend_addr = server_socket2.accept()  # 수신 대기
            msg = client_socket.recv(SIZE)  # client 메세지 반환
            print("[{}] message : {}".format(cliend_addr, msg))

            client_socket.sendall('welcome 5050!'.encode())  # client 응답
            client_socket.close()       # 클라이언트 소켓 종료

