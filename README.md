# Network-Programming

Network Programming Practice<br/>
Following some documents & http://mobilelab.khu.ac.kr/wordpress/fssn/?vid=14<br/><br/>

## Goal:<br/>

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
