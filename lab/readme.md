JMC 2017


---

### W2#02 :: Machine Learning with Python

#### .sh 파일에 대해서

+ `.sh` 확장자로 끝나는 파일 또한 `.py`처럼 파이썬 파일이다.
+ 다만 `abc.py` 파일을 실행하려면 `python abc.py`로 하면 되듯이
+ `abc.sh` 파일을 실행하려면 `bash abc.sh`

---

### W1#01 :: bingo_mod.pyc 파일

#### 캐시 파일이 생기는 이유

1. bingo.py 파일을 실행하면 첫 번째 줄 코드에 의해 bingo_mod 파일을 import한다.
2. 이때 컴퓨터는 bingo_mod 파일을 컴퓨터가 보기 편한 raw한 언어로 바꿔서 bingo_mod.pyc(캐시)파일을 생성한다.
3. bingo_mod.pyc 파일이 생성되면 이후에 bingo.py 파일을 실행했을 때 bingo_mod.pyc가 컴퓨터가 보기 편한 언어로 되어 있으므로 더 빠른 속도로 실행할 수 있다.

#### bingo_mod.py와 bingo_mod.py의 차이점

+ bingo_mod.py : 사람이 스크립트로 작성한 파일
+ bingo_mod.pyc : bingo_mod.py를 컴퓨터가 보기 편한 언어로 바꿔놓은 파일

---
