
---

### EM (20170925)

### 01 EM을 하는 이유

+ 모델의 parameter를 estimation 하려고


### 02 상황 설정

+ 데이터가 2개의 Gaussian에 의해 생성되었다.
  + G1(mu1, sigma1)
  + G2(mu2, simga2)
  + 하지만 각 parameter 값은 모르는 상태이다.
+ 섞여 있는 데이터를 2개의 그룹으로 clustering 하고자 한다.
+ 모델의 paramter 즉, (mu1, sigma2), (mu2, simga2)를 추정해야 한다!

### 03 Democratic Decision

+ P(data | model)
+ 모든 데이터가 참여해서 parameter를 정한다.
+ 그런데 모든 데이터가 동등하게 참여하면 모델1과 모델2의 parameter가 같아지므로 하나마나이다.
+ 따라서 데이터에 가중치를 줘야 한다.

### 04 Gaussian Mixture model

+ Gaussian 모델을 k개 섞어서 하나의 모델로 만든다.

### 05 Expectation Maximization

+ E-step과 M-step을 반복한다.
+ M-step을 하면 모델의 새로운 parameter가 생긴다.
+ 새로운 parameter로 likelihood를 계산한다.

#### E-step

+ Expectation : Expected value of latent variables

#### 가우시안에서 latent variable의 의미

+ 모든 데이터 포인트가 mu_k를 계산할 때 참여하는데, 데이터마다 어느 모델에서 생성되었는지 모르므로 비중을 equally하게 두면 안된다.
+ 각 데이터가 계산에 관여하는 비중이 latent variable이 된다.
+ 각 데이터가 어느 모델에서 생성되었는지를 고려한 값이 latent variable이다.

### 04-1 HMM (Hidden Markov 모델)

+ 어느 코인에서 나왔는지 알고 싶어서 HMM을 사용한다.
+ HMM 모델의 parameter
  + character emission probability
  + state transition probability
+ HMM 모델의 좋고 나쁨의 기준 : likelihood
  + P(data | model)

### latent variable을 사용하는 이유

+ 모델 parameter estimation할 때 어떤 정보가 있어야 가능할까?
+ 즉, latent variable로 무엇을 써야 할까?
+ latent variable을 결정하면 모델 parameter estimation을 할 수 있다.

### HMM의 수는 무한대

+ 가능한 모든 HMM의 수는 무수히 많으므로 불가능
+ 그래서 EM을 사용함

### dynamic programming

+ 작은 문제의 solution을 저장해두고 필요할 때마다 갖다가 쓴다.
+ 즉 작은 문제의 solution을 combine해서 큰 문제의 solution을 구한다.




---

### W3 Decision Tree

#### Pruning

+ decision tree 나무의 키가 크면 안 좋다. overfitting이기 때문에.
+ 그래서 키를 낮춰야 하는데, 이걸 pruning이라 한다.

#### GINI index


#### Decision Tree에서 최적의 tree를 고르는 것에 대한 논의

+ 가장 이상적인 방법은 모든 가능한 tree 모양에서 error가 최소화되는 tree를 선택하는 것이다.
+ 그러나 attribute에 따라 tree가 생성되는 경우의 수는 exponential하게 증가하므로 결국 computation이 불가능하다.
+ 대안
  + 1) 휴리스틱 접근 :
    + 첫번째 level로 어떤 feature가 좋을지 경험적인 지식으로 feature를 선정한다.
    + 그 이후 나눠지는 경우마다 최적의 attribute일 것 같은 feature를 선정한다. (이러한 과정을 **greedy** 알고리즘이라 한다)
    + 이렇게 그때 그때 feature를 선정하는 기준이 heuristic하므로 휴리스틱 접근이라 한다.
  + 2) 지니계수와 같이 scientific하게 접근:
    + 지니계수를 이용하면 수학적인 논리를 사용하므로 quantitative하게 attribute를 한정시킬 수 있다.
    + 따라서 지니계수를 이용하면 attribute의 순서를 수학적인 근거로 정할 수 있고
    + 가능한 tree 모양을 대폭 줄일 수 있다.

> **Note:** greedy 알고리즘 : 한 번 decision을 하고 다음 스텝으로 넘어가면 이전 단계로는 다시 되돌아가지 않는다.

#### QNA. continuous variable

+ continuous variable을 discrete하게 만든다. (=discretize) (맥락 : information entropy)
+ classification과 regression을 합쳐서 한다 (=CART).

#### QNA. variable 간의 상관관계

+ 상관관계가 너무 높은 variable은 없앤다.
+ 상관관계가 있는 것을 한
+ attribute의 위치도 상관관계가 있을 수 있다.
  + 이것을 handle하는 게 딥러닝의 CNN
  + nearby 데이터 고려하기 때문
  + 상관관계 고려하는 게 쉽지 않음 -> 연산의 복잡도 급격 증가 10C2, 10C3, ...
+ 두 variable이 상관관계가 있다고 알려주는 term을 집어넣어서 regression하는 경우도 있다.
+ 거의 모든 classification 알고리즘에서 모든 변수의 상관관계를 한꺼번에 고려하는 것은 거의 없음
+ 그나마 잘 되는 게 CNN

#### 패턴 마이닝

+ 해본 사람마다 하는 이야기 : 아무 의미 없다. rule 십만 개..
+ 왜 rule mining 상관이 없냐?
+ class label하게 상관이 없게 만들기 때문


#### 데이터 마이닝 vs 머신러닝

+

### W3 Information Gain

+ information gain을 알려면 information을 알아야 하고,
+ information을 알려면 entropy를 알아야 한다.

#### Entropy가 무엇인가

+ entropy = uncertainty
+ 엔트로피는 불확실성이다.
+ 그리고 불확실성을 quantify(수치화)한 개념이 엔트로피이다.
+ H(X) = -sigma(pi*logpi)

#### information이 많으면 uncertainty가 줄어든다

+ information = uncertainty가 얼마나 줄었는가 = uncertainty가 줄어든 양
+ I(X) = Hmax - H(X)

#### 엔트로피가 높은지 낮은지에 대한 absolute 기준 있나?

+ 0.9 : 0.1 로 구분되었을 때를 최소한의 decision 기준이라고 생각한 후
+ 0.9 : 0.1 비율을 유지했을 때의 엔트로피를 계산하면 그걸 절대적 기준이라고 유추해볼 수는 있다.

#### 왜 pruning 해야 하나

+ overfitting을 피하기 위해서
+ tree가 너무 tall 하면 training data 외에 predict 불가
+ 우리는 test data에 대해 generalization 되도록 해야 한다

#### 어디를 pruning 하나

+ pruning 했을 때 accuracy가 별로 안 줄어드는 곳

---

### W3 민주적인 방법을 사용하는 tree 3가지

#### Bagging 배깅

+ 데이터를 랜덤하게 샘플링해서 tree를 만들어서 민주적으로 결정을 한다.
+ 데이터를 새로 만들어서
+ Sampling with replacement 민주적인 게 더 낫다

#### Boosting (vs. Bagging)

+ classifier를 만들었는데 accuracy가 90%라고 해보자.
+ 답이 틀린 것은 weight를 더 많이 준다.
+ predictor가 어느 방향으로 가도록

+ 5개 데이터
  + bagging 샘플링 : 평균적으로 비슷하게 샘플링
  + boosting 샘플링 :

> **Note:** Boosting은 수업 자료에 없음

#### Random Forest (노트 필기 참조)


#### Variable Importance

+ 전반적으로 어떤 attribute가 결정하는데 중요한지 variable importance가 설명해준다.
+ Random Forest에서 tree 5,000개 있다고 해보자.
+ tree 5,000개 각각 top level attribute가 있을 것이다.
+ 이런 식으로 tree 전부를 전반적으로 살펴보면 attribute의 중요도를 어느 수준으로 measure할 수 있게 된다.

#### Random Forest vs. Bagging

+ Bagging은 데이터 수를 RF처럼 많이 줄이지 않는다.
+ 대개 attribute도 random sampling 하지 않는다.

#### 3가지 비교

+ bagging과 boosting은 decision tree 외에도 다른 classification에도 쓰인다.
+ random forest는 decision tree에서 3가지 방법 중 가장 잘 정립된 방법이다.

---

### W3 continuous value에 대한 decision tree

#### 1) discretize

+ 톰 미첼 p.77 (http://www.cs.cmu.edu/afs/cs.cmu.edu/project/theo-20/www/mlbook/ch3.pdf)

#### 2) CART

+ regression과 classification 합친 알고리즘
+ 굉장히 powerful한 알고리즘

#### 정리

+ 후반부 수업에서 한 번 더 정리멘트 (rec 20:00, at 14:27)


#### 슈퍼컴퓨터의 architecture

+ 데이터 전처리에 대한 기능이 없음
+ 과거 시뮬레이션 돌리는 작업에 맞춰져 있다 보니 현재 빅데이터 시대에 적절하지 않음

#### 맵리듀스 알고리즘

+

---
---

### W1 :: 수학

+ 로그함수 : 계산하기 매우 어려운 연산에서 로그함수를 적용하면 수치 계산이 쉬워진다.
+ 편미분 : 변수가 여러 개일 때 한꺼번에 미분하지 못하므로 편미분을 한다.
+ 미분 : 최적화 값을 구하기 위해 사용한다.

+ $w^{T}x$ : 계수와 변수의 곱
+ 확률변수의 기대값을 계산할 때 각 값과 값의 확률을 곱해서 더하는데, 여기서 값의 확률이 머신러닝에서는 변수의 중요도가 된다.

### W1 :: 기계학습 개요

#### 선형회귀

+ model
+ 최소제곱법

systematic enumeration : 빼먹지 않고 중복하지 않고 데이터를 찾는다.

#### 최우추정법

+ Casino
+ 주사위 model
  + Fair model (1/6, ..., 1/6)
  + Loaded model (1/10, ..., 1/10, 1/2)
+ P(66666 | Fair) vs. P(66666 | Loaded)
  + Maximum Likelihood

#### Decision Tree

+ 무엇을 먼저 결정할지가 중요하다.
+ 정보 이론

---

#### 1. computability가 중요한 이유

+ 어떤 현상을 계산할 수 있는 model이 있느냐 없느냐가 중요하다
+ 알파고 : 바둑에 대한 model을 세웠다.
+ 감성에 대한 model? 아직 없다.
+ model이 없으면 계산할 수 없다.

#### 2. 사람과 같은 방식으로 model할 필요는 없다.

+ 알파고 : 사람과 다른 방식으로 바둑을 둔다.

---

#### 퍼셉트론

+ 차원을 높여서 데이터를 2개로 구분한다.

#### 딥러닝

+ 퍼셉트론을 네트워크로 연결해서 데이터들의 decision boundary를 결정한다.
+ 인공신경망은 decision boundary에 대한 함수가 무엇인지는 모르나 decision boundary를 구한다.
+ 작동은 되는데 작동의 이유는 알 수 없다.

#### 로지스틱 회귀

+ positive와 negative를 구분하고 싶다.
+ positive data에 대한 모델(M+)을 만든다.
+ negative data에 대한 모델(M-)을 만든다.


+ 회귀: 숫자값을 리턴하는 선형함수
+ 2가지 선형함수의 값을 서로 비교하는 것은 힘들다. ex. 여자 중에 100등과 남자 중에 100등 중 누가 더 뛰어난가? 알 수 없음.

#### K-means

+ 군집을 만든다.

#### K-nearest

+ 가까운 K

#### PCA

+ 변수가 수십 개일 때 전부 다 합쳐서 데이터의 분산이 maximize가 되는 가상의 축을 만들고,
+ 그 가상의 축의 직각으로

### W1 :: 알파고는 바둑을 어떻게 두는가, 랜덤 시뮬레이션

+ 랜덤 시뮬레이션 : pdf를 고려(guide)해서 랜덤하게 추출해야 한다.

+ 가이드란 domain knowledge를 기반으로 한다. 가령 하수의 데이터가 아니라 고수의 데이터를 참고해야 한다는 것이다. (그래서 빅데이터가 중요하다)

> **Note:** 우리나라의 펀드가 미국의 펀드보다 수익률이 낮은 것도 데이터의 양과 질이 부족하기 때문이다.

> **Note:** 거꾸로 우리나라는 전 세계적으로 전국민을 대상으로 의료보험을 하는 유일한 나라이다. 의료보험 데이터로 우리나라가 앞서 가야 한다고 말하는 주장은 설득력이 있는 주장이다.

+ 알파고가 바둑을 두는 메카니즘 : Reinforcement Learning와 simulation이다. 딥러닝이 아니다.

+ 사람은 몇 수 앞을 내다보고 바둑을 두지만, 알파고는 한 판을 다 둬본 후에 바둑을 둔다.
+ 이것을 random simulation이라 한다.
+ 누가 이기겠는가, 당연히 10수 앞을 내다보는 사람보다 한 판을 다 둬 본 기계가 이기게 된다.

### W1 :: 알파고가 바둑을 두는 방법

+ policy : 고수의 수
+ value network : 판세
+ policy network : 각 수에 10만 판을 뒀더니 승률이 어떻게 되는지를 구한 후 가장 많이 이기는 점에 수를 둔다.

---
