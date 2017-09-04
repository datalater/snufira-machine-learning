
ⓒ JMC 2017

---

## 20170904 Lab05

### 01 linear regression vs. logistic regression

| 비교 | linear regression | logistic regression |
| --- | --- | --- |
| 차이점 1 | label 값이 유의미하다 | label 값이 class를 임의의 숫자로 매긴 것이다 |
| 차이점 2 | label 값에 수학적 근거가 있다 | label 값에 수학적 근거가 없다 (= target value를 modeling 하면 안 된다) |
| 차이점 3 | directly model target values | define probability of target values |

### 02 target value의 확률을 구하는 과정

+ 어떤 모델에 input을 넣어서 target value를 예측하는 확률값을 구해야 한다.
+ 특정 input이 여러 class 중 어느 class에 가까운지 알려면, 각 class에 속할 확률의 값을 비교해야 한다.
+ 확률의 값을 비교하려면 odds와 logit이라는 개념을 사용한다.

#### 1) define odds

+ 두 개 확률의 차이나 대소를 비교할 때, 일반적으로 odds(비율)를 사용한다.
+ odds란 event A가 event B보다 상대적으로 더 많이 나올 비율을 뜻한다.
+ odds(A to B) = P(A)/P(B)
  + 만약 사건의 분포가 베르누이 분포라면 (= target value가 2가지라면),
  + odds = P(Y=1)/P(Y=0) = p/(1-p)

#### 2) define logit

+ odd는 양수의 범위를 가지는데, 보통 양수의 범위를 가지는 값을 비교할 때는 log함수를 취한다.
+ odds에 log를 취한 것을 logit이라고 한다.
  + odds에 log를 취하는 이유는 나중에 sigmoid 함수에 input으로 넣으려고 하기 때문이다.
  + sigmod 함수는 exponential 함수이기 때문에 log를 input으로 넣어야 연산이 간단해진다.
+ logit = ln(odds) = ln(p/(1-p))
+ logit의 범위는 -무한대부터 +무한대까지 가능하다.
  + odds는 언제나 양수이고
  + log 함수에서 x > 0이면 함수값의 범위가 -무한대부터 +무한대까지 가능하다.

#### 3) x와 logit의 관계 파악

+ 지금까지 input x에 따라 어떤 logit이 나오는지 계산했다.
+ logit은 모델의 최종 output인 target value를 예측하는 확률값에 쓰이기 때문에
+ x와 target value의 확률값의 관계를 파악하려면
+ x와 logit의 관계를 파악해야 한다.
+ x와 logit의 관계를 선형 모델로 가정해본다.
+ logit = wx + b

#### 4) logit을 linear function으로 modeling 한다

+ 우리가 구해야 하는 최종 output은 x가 P(Y=1)과 같은 특정 class가 될 확률이다.
+ P(Y=1)을 구하려면 x를 input으로 넣어 구한 logit을 이용해야 한다.
+ 그런데 logit의 범위는 -무한대부터 +무한대까지이고 우리가 구하고 싶은 P(Y=1)과 같은 target value의 확률은 0부터 1 사이의 값을 가져야 한다.
+ 따라서 logit을 확률값의 범위인 0부터 1 사이의 값을 가지도록 해야 한다.
+ 어떤 input을 넣어도 0부터 1 사이의 값을 가지는 함수로 sigmoid 함수가 있다.
+ 그래서 logit을 sigmoid 함수의 input으로 넣는다.
+ 그러면 x에서 시작한 값이 logit을 중간 단계로 거쳐서 확률 값으로 변형된다.
+ 즉, x와 P(Y=1)에 대한 그래프를 그릴 수 있게 된다.

#### 99) Model evaluation

+ ROC curve를 그린 다음 AUC를 구한다.


### 기타 :: truncated normal

+ 정규분포에서 데이터를 뽑을 때 구간을 2(or 3)sigma 범위까지만 한정해서 데이터를 샘플링한다.

### explained

+ 숫자 regression : 숫자 자체를 linear model로 만들면 됨
  + f(x) = wb+w1x
+ logistic regression
  + y(=f(x))가 실수가 아니라 category 변수 ex. 0 or 1
  + 0과 1이 나오는 확률을 모델링 해야 함
  + P(Y=1)
  + P(Y=0)
  + odds : P(Y=1)가 P(Y=0) 보다 더 많이 나올 확률 (얼마나 더 큰가)
    + P(Y=1)/P(Y=0)
    + 값의 범위 : 0부터 무한대
  + logit : odd에 log를 씌운 것
    + 값의 범위 : -무한대 부터 +무한대
    + 이것을 선형으로 모델링한다.
  + logit = ln(p/(1-p)) = f(x) ...수업자료 참고

+ softmax 함수의 기저에 있는 분포 : multinomial dist.

### ROC

#### Model evaluation

+ True가 확률을 정해줘야 한다.
+ P(Y=1 | X=x)로 확률을 구함
+ 위에서 구한 확률을 기준으로 어디까지가 True라고 할 것인지 정해줘야 함
+ 그것을 threshold alpha로 정의함


#### ROC 그리는 이유

+ 학습하는 데이터가 bias되어 있어도 AUC는 거의 영향을 받지 않는다.
  + threshold를 일일이 다 적용해서 ROC를 구하므로
+ 단 ROC curve는 binary classification에서만 사용 가능하다.
---


+ multiclass는 threshold를 정하기가 어렵다
+ class가 많을 때는 accuracy를 쓰는 경우가 대부분이다.
+ binary classfication에서는 True를 예측하는 것이 더 중요한 경우가 많다.
  + 질병이 아닌 것보다 질병임(True)을 맞추는 게 목적인 경우가 많다.
  + threshold를 확 낮추면 accuracy가 좋을 순 있으나
  + ex. 100개 중 T:2개 F:98개 있다고 해보자.


### 실습

+ ovr = one-versus-all


---

<<<<<<< HEAD

=======
### W2#02 :: Machine Learning with Python

#### .sh 파일에 대해서

+ `.sh` 확장자로 끝나는 파일 또한 `.py`처럼 파이썬 파일이다.
+ 다만 `abc.py` 파일을 실행하려면 `python abc.py`로 하면 되듯이
+ `abc.sh` 파일을 실행하려면 `bash abc.sh`

---

### W1#01 :: bingo_mod.pyc 파일

#### 캐시 파일이 생기는 이유
>>>>>>> d2c7711b161abc8d982dcd23b1087a85a5da9e1e



<<<<<<< HEAD
=======
+ bingo_mod.py : 사람이 스크립트로 작성한 파일
+ bingo_mod.pyc : bingo_mod.py를 컴퓨터가 보기 편한 언어로 바꿔놓은 파일
>>>>>>> d2c7711b161abc8d982dcd23b1087a85a5da9e1e

---
