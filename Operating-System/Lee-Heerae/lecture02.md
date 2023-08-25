# [System Structure & Program Execution 1](https://core.ewha.ac.kr/assets/publish/C0101020140311132925816476)

## Mode bit

- 사용자 프로그램의 잘못된 수행으로 다른 프로그램에 피해가 가지 않도록 하는 보호 장치
- 하드웨어적으로 두 가지 모드의 operation 지원
    - 1 : 사용자 모드
    - 0 : 모니터 모드
- 보안을 해칠 수 있는 중요한 명령어는 모니터 모드에서만 가능한 특권명령으로 규정
- interrupt나 exception 발생 시 하드웨어가 mode bit 0으로 변경
- 사용자 프로그램에게 CPU를 넘기기 전에 mode bit 1로 세팅

## Timer

- 정해진 시간이 흐른 뒤 운영체제에 제어권이 넘어가도록 인터럽트를 발생시킴
- 매 클럭 때마다 1씩 감소
- 타이머 값이 0이 되면 타이머 인터럽트 발생
- CPU를 특정 프로그램이 독점하는 것을 방지
- time sharing을 구현하기 위해 널리 이용됨
- 현재 시간을 계산하기 위해서도 사용

## I/O device controller

- I/O 장치 유형을 관리하는 일종의 작은 CPU
- 제어 정보를 위해 control register, status register를 가짐
- local buffer 가짐 → 일종의 data register
- I/O는 실제 device와 local buffer 사이에서 일어남
- Device Controller는 I/O가 끝났을 경우 interrupt로 CPU에 그 사실을 알림
- device driver (장치 구동기) :  OS Code 중 각 장치별 처리 루틴을 의미 → software 영역
- device Controller (장치 제어기) : 각 장치를 통제하는 일종의 작은 CPU → hardware 영역

## 입출력(I/O)의 수행

- 모든 입출력 명령은 특권 명령
- 시스템 콜(system call) : 사용자 프로그램이 운영체제에 I/O 요청
- 수행 과정
    - trap을 사용하여 인터럽트 벡터의 특정 위치로 이동
    - 제어권이 인터럽트 벡터가 가리키는 인터럽트 서비스 루틴으로 이동
    - 올바른 I/O 요청인지 확인 후 수행
    - I/O 완료 시 제어권을 시스템 콜 다음 명령으로 옮김

## Interrupt

- 인터럽트 당한 시점의 레지스터와 program counter를 저장한 후 CPU의 제어를 인터럽트 처리 루틴에 넘김
- 인터럽트 종류
    - 하드웨어 인터럽트 - 하드웨어가 발생시킨 인터럽트
    - 소프트웨어 인터럽트 (trap)
        - exception : 프로그램이 오류를 범한 경우
        - system call : 프로그램이 커널 함수를 호출하는 경우
- 인터럽트 용어
    - 인터럽트 벡터
        - 해당 인터럽트의 처리 루틴 주소를 가지고 있음
    - 인터럽트 처리 루틴
        - 해당 인터럽트를 처리하는 커널 함수

## System call

- 사용자 프로그램이 운영체제의 서비스를 받기 위해 커널 함수를 호출하는 것
