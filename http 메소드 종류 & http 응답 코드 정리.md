http 메소드 종류 & http 응답 코드 정리

GET : GET request-url)



| HTTP Method | 전송 형태                                                    | 설명                                                         |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| GET         | GET [request-uri]?query_stringHTTP/1.1\r\nHost:[Hostname] 혹은 [IP] \r\n | URI(URL)가 가진 정보를 검색하기 위해 서버 측에 요청하는형태이다 (서버의 Resource를 읽음) |
| POST        | POST [request-uri]?query_stringHTTP/1.1\r\nHOST:[Hostname] 혹은 [IP] \r\nContent-Lenght:[Lenght in Bytes] \r\n \r\n[query-string] 혹은 [데이터] | 요청 URI(URL)에 폼 입력을 처리하기 위해 구성한 서버 측 스크립트(ASP, PHP, JSP 등) 혹은 CGI 프로그램으로 구성되고 Form Action과 함께 전송되는데, 이때 헤더 정보에 포함되지 않고 데이터 부분에 요청 정보가 들어가게 된다. |
| HEAD        | HEAD [request-uri] HTTP/1.1\r\nHost:[Hostname] 혹은 [IP] \r\n | GET과 유사한 방식이나 웹 서버에서 헤더 정보 (Body) 이외에 어떤 데이터도 보내지(Return) 않는다. 웹 서버의 다운 여부 점검(Health Check)이나 웹 서버 정보(버전 등)등을 얻기 위해 사용될 수 있다. |
| OPTIONS     | OPTIONS [request-ri]HTTP/1.1\r\nHost:[Hostname] 혹은 [IP] \r\n | 해당 메소드를 통해 시스템에서 지원되는 메소드 종류를 확인할 수 있다. |
| PUT         | PUT [request-uri] HTTP/1.1\r\nHost:[Hostname] 혹은 [IP] \r\nContent-Lenght:[Length in Bytes] \r\nContent-Type:[Content Type] \r\n\r\n[데이터] | POST와 유사한 전송 구조를 가지기 때문에 헤더 이외에 메시지(데이터)가 함께 전송된다.원격지 서버에 지정한 콘텐츠를 저장하기 위해 사용되며 홈페이지 변조에 많이 악용되고 있다. |
| DELETE      | DELETE [request-uri] HTTP/1.1\r\nHost:[Hostname] 혹은 [IP] \r\n\r\n | 원격지 웹 서버에 파일을 삭제하기 위해 사용되며 PUT과는 반대 개념의 메소드이다. |
| TRACE       | TRACE [request-uri] HTTP/1.1\r\nHost:[Hostname] 혹은 [IP] \r\n\r\n | 원격지 서버에 Loopback(루프백) 메시지를 호출하기 위해 사용된다. |
| CONNECT     | CONNECT [request-uri] HTTP/1.1\r\nHost:[Hostname] 혹은 [IP] \r\n\r\n | 웹 서버에 프락시 기능을 요청할 때 사용된다.                  |

 

 

| 응답 코드 | 설명                                                         |
| --------- | ------------------------------------------------------------ |
| **1xx**   | **정보제공**                                                 |
| 100       | Continue (클라이언트로 부터 일부 요청을 받았으며 나머지 정보를 계속 요청함) |
| 101       | Switching protocols                                          |
| **2xx**   | **성공**                                                     |
| 200       | OK(요청이 성공적으로 수행되었음)                             |
| 201       | Created (PUT 메소드에 의해 원격지 서버에 파일 생성됨)        |
| 202       | Accepted(웹 서버가 명령 수신함)                              |
| 203       | Non-authoritative information (서버가 클라이언트 요구 중 일부만 전송) |
| 204       | No content, (사용자 요구 처리하였으나 전송할 데이터가 없음)  |
| **3xx**   | **리다이렉션**                                               |
| 301       | Moved permanently (요구한 데이터를 변경된 타 URL에 요청함)   |
| 302       | Not temporarily                                              |
| 304       | Not modified (컴퓨터 로컬의 캐시 정보를 이용함, 대개 gif 등은 웹 서버에 요청하지 않음) |
| **4xx**   | **클라이언트요청오류**                                       |
| 400       | Bad request (사용자의 잘못된 요청을 처리할 수 없음)          |
| 401       | Unauthorized (인증이 필요한 페이지를 요청한 경우)            |
| 402       | Payment required(예약됨)                                     |
| 403       | Forbidden (접근 금지, 디렉터리 리스팅 요청 및 관리자 페이지 접근 등을 차단) |
| 404       | Not found, (요청한 페이지 없음)                              |
| 405       | Method not allowed (혀용되지 않는 http method 사용함)        |
| 407       | Proxy authentication required (프락시 인증 요구됨)           |
| 408       | Request timeout (요청 시간 초과)                             |
| 410       | Gone (영구적으로 사용 금지)                                  |
| 412       | Precondition failed (전체 조건 실패)                         |
| 414       | Request-URI too long (요청 URL 길이가 긴 경우임)             |
| **5xx**   | **서버응답오류**                                             |
| 500       | Internal server error (내부 서버 오류)                       |
| 501       | Not implemented (웹 서버가 처리할 수 없음)                   |
| 503       | Service unnailable (서비스 제공 불가)                        |
| 504       | Gateway timeout (게이트웨이 시간 초과)                       |
| 505       | HTTP version not supported (해당 http 버전 지원되지 않음)    |

