# PCB, Context Switching

##### Process Management

프로세스가 여러개일 때, CPU가 스케줄링을 통해 관리하는 것을 말함

이때, CPU는 각 프로세스들이 누군지 알아야 함. -> 프로세스의 특징을 갖고 있는것이 Process Metadata

- Process Metadata
  
  - Process ID
  
  - Process State
  
  - Process Priority
  
  - CPU Registers
  
  - Owner
  
  - CPU Usage
  
  - Memory Usage
  
  이 메타데이터는 프로세스가 생성되면 PCB에 저장됨
  
  ### PCB(Process Control Block)
  
  프로세스 메타데이터들을 저장해 놓는 곳, 한 PCB 안에는 한 프로세스의 정보가 담김
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-01-19-15-31-08-image.png)

##### PCB가 필요한 이유

CPU에서는 프로세스의 상태에 따라 교체 작업이 이루어짐. 이때, 앞으로 다시 수행할 대기 중인 프로세스에 관한 저장 값을 PCB에 저장하두는 것

##### PCB 관리법

Linked List 방식으로 관리함

PCB List Head에 PCB들이 생성될 때마다 붙게 된다. 주소값으로 연결이 이루어져 있는 연결 리스트라 삽입 삭제가 용이

즉, 프로세스가 생성되면 해당 PCB가 생성되고 프로세스 완료시 제거됨

### Context Switching

CPU가 이전의 프로세스 상태를 PCB에 보관하고, 또 다른 프로세스의 정보를 PCB에 읽어 레지스터에 적재하는 과정

보통 인터럽트가 발생하거나, 실행중인 CPU 사용 허가시간을 모두 소모하거나, 입출력을 위해 대기해야 하는 경우 발생

##### Context Switching의 OverHead란?

CPU에 계속 프로세스를 수행시키도록 하기 위해서 다른 프로세스를 실행시키고 Context Switching을 하는 것

CPU가 놀지 않도록 만들고, 사용자에게 빠르게 일처리를 제공해주기 위한 것.
