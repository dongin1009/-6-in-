# 원격 저장소

remote repository

: locally repository와 대비되는 개념 - 자신의 컴퓨터에서 commit, 저장되는곳 = 저장소

인터넷의 어딘가에 올려 backup, 저장소에 어딘가를 매개로 하여 협업 - 자신의 컴퓨터가 아닌 

1. 버전을 백업(소스코드를 백업)
2. 다른사람과 협업

프로젝트가 커져가면서 중요한 요소.

ex) 드롭박스, 구글드라이브 - 혼자서 할때는 무방



## 원격저장소의 기초

```
git init a
```

a 라는 폴더를 만들고 git 저장소로 지정한다.



```
git init --bare
```

A 폴더를 만들고 working directory로 지정한다.

`--bare` : 작업을 할 수 없고 저장소만으로써의 역할. 수정이 불가능하고 원격 저장소를 만들때 사용한다.

bare:맨살, 벌거벗은



```
git A add origin a
```

`origin`경로를 상대 주소로 변경.



```
git config --global push.default simple
```

push 형식을 simple방식 (어디에서 어디로 지정한 명령어만 push한다 고 설정



```
git push --set-upstream origin master
```

 push 할 때 branch 를 master로 설정한다.

set upstream : master에서 push하면 origin master 로 push 한다.

지역저장소 와 원격 저장소를 설정.



## 원격 저장소를 지역 저장소로 복제(Github)

Fork : 자기 Github로 복제.



```
git clone <주소> gitsrc
```

원격 저장소<주소> 의 파일들을 지역 저장소로 가져온다.(clone)



```
git log --reverse
```

`--reverse`:거꾸로



```
git checkout 'commit id'
```

> commit id 로 checkout 한다.



## 원격 저장소 만들기(Github)

원격저장소 -> 로컬저장소



로컬저장소 -> 원격저장소



```
git remote add origin 'github주소'
```

origin 이라고 별명을 붙임

git remote

remote 목록을 보여줌

git remote -v

상세 remote 목록을 보여줌



```
git remote --help
```

git remote 설명

```
git remote remove A
```

A 원격저장소 삭제

```
git push -u origin master
```

origin과 master를 동기화한 후 push 한다.

`-u`:이름과 주소 동기화. 최초 1회만 실행.



## 원격 저장소와 지역 저장소의 동기화 방법 (Github)

```
git commit --amend
```

push 전 가장 최근의 commit을 수정 할 수 있음

```

```

원격 저장소의 최근 commit 내용을 땡겨옴.

원격 저장소 -> 지역 저장소



## 로그인 없이 원격 저장소 이용하기(Github)

ssh :  Secure SHell

HTTPS : push를 할 때 마다, 원격 저장소에 접근 할때 마다 id와 password필요

SSH : 자동으로 로그인.

```
ssh-keygen
```

ssh를 통해 다른컴퓨터 접근 위한 비밀번호 생성

보안에 강력

```
cd ~/.ssh
```

자신의 홈디렉토리의 .ssh폴더로



id_rsa  :  private key - 본인의 컴퓨터에만 저장

id_rsa.pub  :  public key - 접근하려는 서버 컴퓨터에 전송





github-settings-SSH and GPG keys-New SSH key-<Key> 부분에 id_rsa.pub 의 값을 붙여넣기-Add SSH key

웹을 통해서 서버 컴퓨터인 github 원격저장소에 public key를 저장. 

id_rsa.pub 와 id_rsa 가 짝이므로 id_rsa를 가지고 있는 개인 컴퓨터에 접근 가능



## 자기 서버에 원격 저장소 만들기 (My Server)

```
git init --bare remote
```

remote라는 저장소를 만든다.

```bash

```

원격으로 접속

```bash
git clone ssh://git@13.124.42.13/home/git/git/remote/ office
```

office라는 directory 로 원격 저장소에 있는 파일을 가져온다.(동기화)



## push & pull (My Server)

똑같은 원격 저장소에 연결되어 있는 서로 다른 컴퓨터(지역 저장소)일 때

git push(올리기) 와 git pull(내리기) 를 통해 분산 버전 관리 시스템을 사용할 수 있다.



## 자동 로그인 (My Server)

```bash
ssh-keygen -t rsa
```

rsa 방식의 ssh keygen 을 생성한다.

private key(id_rsa)를 가지고 있는 컴퓨터는 public key(id_rsa.pub)를 가지고 있는 서버 (컴퓨터)에 접근할 수 있다.

그래서 public key를 가지고 있는 서버에는 자동 로그인 (authorized_keys) 이 가능하게 할 수 있다.

```bash
ssh-copy-id git@13.124.42.13
```

public key 를 자동 복사 하여 자동 로그인 파일(authorized_keys)을 만든다.