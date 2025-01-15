# [PCCE 기출문제] 번 / 
## 문제 설명
퓨쳐종합병원에서는 접수한 환자가 진료받을 병과에 따라 자동으로 환자 코드를 부여해 주는 프로그램이 있습니다.
환자 코드의 마지막 네 글자를 보면 환자가 어디 병과에서 진료를 받아야 할지 알 수 있습니다.
예를 들어 환자의 코드가 "_eye"로 끝난다면 안과를, "head"로 끝난다면 신경외과 진료를 보게 됩니다.
환자 코드의 마지막 글자에 따른 병과 분류 기준은 다음과 같습니다.

|마지막 글자|병과|
|----------|----|
|"_eye"|"Ophthalmologyc|
|"head"|"Neurosurgery"|
|"infl"|"Orthopedics"|
|"skin"|"Dermatology"|

환자의 코드를 나타내는 문자열 `code`를 입력받아 위 표에 맞는 병과를 출력하도록 빈칸을 채워 코드를 완성해 주세요. 
위 표의 단어로 끝나지 않는다면 "direct recommendation"를 출력합니다.

## 제한사항
- 4 ≤ code의 길이 ≤ 20
- `code`는 영어 소문자와 숫자, 언더바("_")로 이루어져 있습니다.

## 입출력 예
### 입력 #1
```python
dry_eye
```
### 출력 #1
```python
Ophthalmologyc
```
### 입력 #2
```python
pat23_08_20_head
```
### 출력 #2
```python
Neurosurgery
```

## 입출력 예 설명
### 입출력 예 #1
- `code`가 "_eye"로 끝나기 때문에 "Ophthalmologyc"를 출력합니다.
### 입출력 예 #2
- `code`가 "head"로 끝나기 때문에 "Neurosurgery"를 출력합니다.

## solution.py
```python
code = input()
last_four_words = code[-4:]

if last_four_words == "_eye" :
    print("Ophthalmologyc")
elif last_four_words == "head" :
    print("Neurosurgery")
elif last_four_words == "infl" :
    print("Orthopedics")
elif last_four_words == "skin" :
    print("Dermatology")
else :
    print("direct recommendation")
```

## 해설
1. if-elif-else를 활용하는 문제이다.
2. `code`의 맨 끝 4글자를 `last_four_words`에 저장했으므로, `문제설명`란의 마지막 글자에 해당하는 `elememt`들을 `if-elif` 문으로 구현한다.
3. 마지막 `else`로 표에 포함되지 않는 환자코드를 처리한다.
