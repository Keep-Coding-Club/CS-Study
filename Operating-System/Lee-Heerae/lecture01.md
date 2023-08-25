# [Introduction to Operating Systems](https://core.ewha.ac.kr/assets/publish/C0101020140307151724641842)

## 운영체제(OS, Operating System)

- 컴퓨터 하드웨어 바로 위에 설치되어 사용자 및 다른 모든 소프트웨어와 하드웨어를 연결하는 소프트웨어 계층
- 크게는 커널을 포함한 주변 유틸리티까지 작게는 커널만 의미
- 역할 및 목적
    1. 컴퓨터 시스템의 자원을 효율적으로 관리하기 위해
    2. 사용자 및 컴퓨터 보안을 위해
    3. 컴퓨터 시스템을 편하게 사용할 수 있는 환경을 제공해 줌

## 운영체제의 분류

- 동시 작업 가능 여부
    - 단일 작업 - single tasking
    - 다중 작업 - multi tasking
- 사용자의 수
    - 단일 사용자 - single user
    - 다중 사용자 - multi user
- 처리 방식
    - 일괄처리 - batch processing
    - 시분할 방식 - time sharing
        - 빠르게 처리하면서 동시에 주어진 자원을 최대한 활용하는 OS
        - 사람에게 특화되어 있음
    - 실시간 - realtime OS
        - 정해진 시간 이내에 일이 반드시 종료됨을 보장하는 OS
            - Hard realtime system - 데드라인을 확실히 지켜야 함
            - Soft realtime system - 데드라인을 지키지 않아도 됨

## 운영체제 예

- Unix
    - 최소한의 커널 구조를 가지고 프로그램 개발에 용이하게 만들어진 C언어 기반 운영체제
    - 확장성이 높고 오픈소스임 → 다양한 버전 존재
- Window
    - 단일 사용자용 운영체제
    - PC에 적합
    - Plug and Play
    - 네트워크 환경 강화
    - 풍부한 지원 소프트웨어가 존재함
