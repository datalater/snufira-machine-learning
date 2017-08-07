JMC 2017


---

### W1#01 :: bingo_mod.pyc 파일

#### 생기는 이유

1. bingo.py 파일을 실행하면 첫 번째 줄 코드에 의해 bingo_mod 파일을 import한다.
2. 이때 컴퓨터는 bingo_mod 파일을 컴퓨터가 보기 편한 raw한 언어로 바꿔서 bingo_mod.pyc(캐시)파일을 생성한다.
3. bingo_mod.pyc 파일이 생성되면 이후에 bingo.py 파일을 실행했을 때 bingo_mod.pyc가 컴퓨터가 보기 편한 언어로 되어 있으므로 더 빠른 속도로 실행할 수 있다.

#### bingo_mod.py와 bingo_mod.py의 차이점

+ bingo_mod.py : 사람이 스크립트로 작성한 파일
+ bingo_mod.pyc : bingo_mod.py를 컴퓨터가 보기 편한 언어로 바꿔놓은 파일
