# 질문

## 김선경

## 박은비

## 유다영

1. IEEE 802.11 (Wi-Fi) Frame에서 3개의 address field (잘 안 쓰이는 4번째 제외)가 각각 무슨 주소를 의미하는지, 그리고 왜 3개의 address field가 필요한지 설명하시오.
2. 멀티미디어를 스트리밍하는 방법으로, HTTP 에서 서버가 영상 파일을 여러개의 chunk로 나눠 저장하고 클라이언트는 네트워크 상황에 맞춰 데이터 전송 속도를 조절하는 실시간 영상 재생 방법을 무엇이라 하는가?
3. HTTP의 무상태와 비연결성에 대해 설명하시오.

## 이희래

# 모범답안

## 김선경

## 박은비

## 유다영

1.  IEEE 802.11 (Wi-Fi) Frame에서 3개의 address field (잘 안 쓰이는 4번째 제외)가 각각 무슨 주소를 의미하는지, 그리고 왜 3개의 address field가 필요한지 설명하시오.

    1. address 1: 해당 frame을 수신하는 interface의 MAC address
    2. address 2: 해당 frame을 전송하는 interface의 MAC address
    3. address 3: 해당 frame을 처리하는 router의 MAC address

    3개의 주소 필드는 무선 네트워크에서 데이터를 정확하게 라우팅하고, 여러 디바이스 간의 동시 통신을 지원하며, 무선 네트워크 구조를 관리하는 데 필요합니다. 이를 통해 무선 네트워크가 효율적으로 동작할 수 있게 됩니다.

2.  멀티미디어를 스트리밍하는 방법으로, HTTP 에서 서버가 영상 파일을 여러개의 chunk로 나눠 저장하고 클라이언트는 네트워크 상황에 맞춰 데이터 전송 속도를 조절하는 실시간 영상 재생 방법을 무엇이라 하는가?
    **DASH(Dynamic Adaptive Streaming over HTTP)**

    멀티 미디어 스트리밍 업체는 서버에서 비디오를 통째로 인코딩하는 것이 아니라

    1. 작은 chunck 단위로 분리
       - 각 chunck는 여러 개의 코딩 rate(128kbps, 256kbps, ..)로 인코딩
       - manifest file: 각 chunck가 저장되어 있는 URL 주소
    2. 클라이언트의 네트워크 상황에 맞는 chunck 를 순서대로 재생시킴.
       - 네트워크 속도가 안 나오기 시작하면 코딩 rate를 낮춘 chunck를 제공한다(Dynamic)

3.  HTTP의 무상태와 비연결성에 대해 설명하시오.

    **무상태** 프로토콜이란 서버가 클라이언트의 상태를 저장하지 않는 특징이다.

    서버의 확장성에 용이하다는 장점이 있지만, 클라이언트가 **추가 데이터**를 전송해야 하는 단점이 있다.

    로그인이 필요 없는 단순한 서비스 소개 화면 같은 경우엔 무상태로 설계할 수 있지만, 로그인이 필요한 서비스라면 유저의 상태를 유지해야 되기 때문에 브라우저 쿠키, 서버 세션, 토큰 등을 이용해 상태를 유지한다.

    HTTP 1.0 기준으로, **비연결성**을 가지는 **HTTP**에서는 실제로 요청을 주고받을 때만 연결을 유지하고 응답을 주고 나면 TCP/IP 연결을 끊는다. 최소한의 자원으로 서버를 유지한다.

    **하지만, 트래픽이 많고, 큰 규모의 서비스를 운영할 때에는 비연결성은 한계가 있다.**

    웹 브라우저로 사이트를 요청하면 HTML뿐만 아니라 자바스크립트, css, 추가 이미지 등 수많은 자원이 함께 다운로드된다. 해당 자원들을 각각 보낼 때마다 연결 끊고 다시 연결하고를 반복하는 것은 비효율적이기 때문에 **HTTP 지속 연결(Persistent Connections)로 문제를 해결**한다.

## 이희래