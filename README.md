# Socket-Programming

Socket Programming Practice w/Python&amp;C <br/>
Following https://realpython.com/python-sockets/ and http://mobilelab.khu.ac.kr/wordpress/fssn/?vid=14<br/><br/>

### Goal:<br/>

#### 1. Socket 통신 제대로 이해하기

#### 2. Python -> C

### Execution

#### shell #1

`python echo-server.py`
<br/>

#### shell #2

`python echo-client.py`
<br/>

#### output in shell #1

- Connected by ('127.0.0.1', 56522)
  <br/>

#### output in shell #2

- Received b'Hello, world'
  <br/><br/>

### Viewing Socket State

`netstat -an`

#### 이미 LISTENING 상태인 포트를 쓰고 싶다면?

- Get PID
  `Get-Process -Id (Get-NetTCPConnection -LocalPort 포트#).OwningProcess`
  <br/>
  -> KILL
  `taskkill /F /PID PID#`
