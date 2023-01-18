# Blocking I/O & Non-Blocking I/O

I/O 작업은 Kernel level에서만 수행할 수 있다. 따라서, Process, Thread는 커널에게 I/O를 요청해야 한다.

### Blocking I/O

1. Process(Thread)가 Kernel에게 I/O를 요청하는 함수를 호출

2. Kernel이 작업을 완료하면 작업 결과를 반환 받음.

특징

- I/O 작업이 진행되는 동안 user Process(Thread)는 자신의 작업을 중단한 채 대기

- Resource 낭비가 심함 (I/O 작업이 CPU 자원을 거의 쓰지 않음)

여러 클라이언트가 접속하는 서버를 Blocking 방식으로 구현하는 경우
I/O 작업을 진행하는 작업을 중지
다른 클라이언트가 진행중인 작업을 중지하면 안되므로, 클라이언트별로 별도의 Thread 생성
이로 인해, 많아진 Thread로 컨텍스트 스위칭 횟수가 증가함

### Non-blocking I/O

1. user Process가 recvfrom 함수 호출(커널에게 해당 소켓으로부터 data를 받고싶다고 요청)

2. Kernel은 이 요청에 대하여 곧바로 recvBuffer를 채워 보내지 못하므로 'EWOULDBLOCK'을 리턴함.

3. Blocking 방식과 달리, user Process는 다른 작업을 진행할 수 있음.

4. recvBuffer에 user가 받을 수 있는 데이터가 있는 경우, Buffer로부터 데이터를 복사하여 받아옴.
   이때, recvBuffer는 Kernel이 가지고 있는 메모리에 적재되어 있으므로, Memory간 복사로 인해 I/O보다 훨씬 빠른 속도로 data를 받아올 수 있음.

5. recvfrom 함수는 빠른 속도로 data를 복사한 후, 복사한 data의 길이와 함께 반환


