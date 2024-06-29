# Network-Programming

Network Programming Practice<br/>
Following some documents & http://mobilelab.khu.ac.kr/wordpress/fssn/?vid=14<br/><br/>

## Goal:

Information Exchange

### [L4] Socket Programming w/Python

- `python echo-server.py` <br/>
- `python echo-client.py` <br/>
- `netstat -an` - Viewing Socket State <br/><br/>

[realpython/python-sockets](https://realpython.com/python-sockets/) <br/>
[Socket Programming w/C](https://www.geeksforgeeks.org/socket-programming-cc/)

#### 이미 LISTENING 상태인 포트를 쓰고 싶다면?

- Get PID
  `Get-Process -Id (Get-NetTCPConnection -LocalPort 포트#).OwningProcess`
  <br/>
  -> KILL
  `taskkill /F /PID PID#`

---

### [L7] Zero Message Queue

Kernel -> Application

<br/><br/>

[ZeroMQ](https://zeromq.org/)<br/>
[ZeroMQ Github](https://github.com/zeromq)<br/>
[PyPI pyzmq](https://pypi.org/project/pyzmq/)

---

### [L7] HTTP

메시지 기반 요청 - 응답 구조

- Resources: Media-Types (Content-type, ..), URI
- Transactions: HTTP Methods, Status Code
- Methods: GET, HEAD, PUT, POST, TRACE, OPTIONS, DELETE
- Monolithic vs SOA vs Microservice
- SOAP(XML) vs REST(JSON)

#### /1.1

- Connections: HTTP over TCP/IP and TLS/SSL, Proxy
- GET(R), PUT(U), POST(C), DELETE(D)

#### /2

- gRPC
  HTTP/2, RPC기반 Protobuf 활용 통신<br/>
  [learn.microsoft - gRPC 서비스와 HTTP API 비교](https://learn.microsoft.com/ko-kr/aspnet/core/grpc/comparison?view=aspnetcore-8.0)<br/>
  [Python Microservices With gRPC](https://realpython.com/python-microservices-grpc/)

- HTTP/2
  Google SPDY - 구글의 비표준 네트워크 프로토콜 <br/>
  - binary framing layer 도입
  - 지연시간 감소, 응답 다중화, 헤더필드 압축, 우선순위 지정, 서버 푸시
    [Go http2 package](https://pkg.go.dev/golang.org/x/net/http2)<br/>
    [Certificates for localhost](https://letsencrypt.org/docs/certificates-for-localhost/)

#### /3

UDP 위에서 동작하는 (+ TCP에 상응하는) **QUIC**[L4]<br/>
[QUIC Working Group](https://quicwg.org/)<br/>

#### Summary

1. HTTP/1.1 - ASCII over TCP
2. HTTP/2 - Binary multiplexed over TCP
3. HTTP/3 Binary over Multiplexed QUIC

### WebRTC

Web P2P Real Time Communication<br/>

[webrtc.org](https://webrtc.org/)<br/>
[mdn web docs > Web APIs > WebRTC API](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API)
