# branch

- 나무의 가지

- 하나의 기둥(main 작업)에 가지(사용자별, 기능별, 개발자별 등등..)를 쳐서 작업에 용이 - 추가, 제거, 버그체크 등...

  ```
  git branch
  ```

  분기 상태 리스트 (현재 분기는 앞에 * 표시)


## branch 만들기

```
git branch A
```

`A` branch 생성.

branch 생성 전 상태, 내용을 그대로 복사



```
git checkout A
```

현재의 branch에서 나가고 `A`로 바뀜

숙소의 체크아웃 개념



```
git commit -am "first"
```

`commit` 단계에서 자동으로 `add`까지 수행. 하지만 한번도 `add`를 하지않은 파일의 경우 불가.



## branch 정보확인

```
git log --branches --decorate
```

현재 branch(*)를 포함한 모든 branch의 `log`를 보여줌



- `HEAD` : '현재의 branch'



```
git log --branches --decorate --graph
```

`git log --branches --decorate` 기능에 색깔 줄로 branch들간의 `commit` 공통점과 차이점을 보여줌

- `--graph` : 색깔 줄(그래프)로 공통점과 차이점을 표시



```
git log branches --decorate --graph -- oneline
```

`git log --branches --decorate --graph` 기능을 한 줄로 전체적인 상황을 볼 수 있다.

- `--oneline` : 차이점만 한 줄로 표시



```
stree
```

source tree 라는 프로그램(설치 필요)을 통해 GUI로 보여줌



```
git log master..A
```

`master`에는 없고 `A` 에만 있는 `commit`을 보여줌



```
git log -p master..A
```

`master`에는 없고 `A`에만 있는 `commit`과 코드를 보여줌

- `-p` : 코드를 포함



```
git diff master..A
```

`master`와 `A`  간의 코드, 파일의 차이점을 보여줌



## branch 병합

- ###### A => master(*) 을 하고자 할때

  1. `A` 에서 `master`로 `checkout` 한다.

     ```
     git checkout master
     ```

  2. `A`와 `merge`

     ```
     git merge A
     ```

  3. (필요에 따라) `A` 삭제

     ```
     git branch -d A
     ```



```
git checkout -b A
```

branch  `A`를 만들고 `A`로 바꾼다. = `git branch A` + `git checkout A`



## branch 병합시 충돌 해결

1.

![A simple commit history.](https://git-scm.com/book/en/v2/images/basic-branching-1.png)

```
git commit "C0"
git commit "C1"
git commit "C2"
```

`master` 에서 `commit` 을 3회 한다.





2.![Creating a new branch pointer.](https://git-scm.com/book/en/v2/images/basic-branching-2.png)

```
git branch iss53
git checkout iss53
```

or

```
git checkout -b iss53
```

`iss53` branch 를 만들고 `iss53`으로 바꾼다.



- `master` 와 `iss53`은 `C2`의 내용


3.

![The `iss53` branch has moved forward with your work.](https://git-scm.com/book/en/v2/images/basic-branching-3.png)

```
vim ex1.txt
git commit -am 'C3'
```

`ex1.txt` 파일을 만들고 `add`, `commit` 한다.

- `master`는 `C2`, `iss53`은 `C3`의 내용



4.

```
git checkout master
```

`master` 로 바꾼다.

![Hotfix branch based on `master`.](https://git-scm.com/book/en/v2/images/basic-branching-4.png)

```
git checkout -b hotfix
vim ex1.txt
git commit -am 'C4'
```

새로운 branch `hotfix`(긴급한 수정 사항)를 만들고 들어간 후 `ex1.txt`파일을 임의로 수정한 후 `commit`한다.

- `hotfix`는 `C2`에 `C4`의 내용 추가


5.

![`master` is fast-forwarded to `hotfix`.](https://git-scm.com/book/en/v2/images/basic-branching-5.png)

```
git checkout master
git merge hotfix
```

`master`로 넘어와 `hotfix`를 병합한다.

- `master`가 `C4`의 내용을 받음.



6.

![Work continues on `iss53`.](https://git-scm.com/book/en/v2/images/basic-branching-6.png)

```
git checkout iss53
vim ex1.txt
git commit -am 'C5'
```

`iss53`으로 돌아와서 `ex1.txt`파일을 (`hotfix`와는 다르게) 임의로 수정한 후 `add` 및 `commit`

- 



## stash

- 감추다, 숨겨주다

- 하나의 작업 중 다른 branch 로 넘어가 작업을 해야할 때, 하지만 `commit`을 하기 애배할 때

- 일종의 임시기억장소 개념

-  LIFO방식으로 가장 늦게(가장 최근에) 들어간 것이 가장 먼저(가장 위에) 나온다.




```
git stash
```

현재 진행중인 작업을 가장 최근 `commit` 상태로 바꾼다.



```
git stash apply
```

가장 최근의 `stash`로 복원한다.



```
git stash list
```

`stash` 한 목록. LIFO 방식



```
git reset --hard HEAD
```

가장 최근 `commit` 상태(`HEAD`)로 복원. 가장 최근 `commit` 상태 (`HEAD`) 이후의 내용은 삭제



```
git stash drop
```

가장 최근에 한 `stash` 삭제



```
git stash apply; git stash drop;
```

or

```
git pop
```

(가장 최근에 한) `stash`로 복원 한 후 `stash` 목록에서 삭제한다.



- tracked 되고 있는 파일 (`commit`에 속해있는 파일)은 `stash`할 수 있지만, untracked 되고 있는 파일(최근 `commit`이후 새로 생성한 파일)은 `stash` 할 수 없다.