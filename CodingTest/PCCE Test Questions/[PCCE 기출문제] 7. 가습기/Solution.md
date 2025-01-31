# [PCCE 기출문제] 7번 / 가습기
## 문제 설명
상우가 사용하는 가습기에는 "auto", "target", "minimum"의 세 가지 모드가 있습니다. 가습기의 가습량은 0~5단계로 구분되며 각 모드 별 동작 방식은 다음과 같습니다.

- "auto" 모드
  - 습도가 0 이상 10 미만인 경우 : 5단계
  - 습도가 10 이상 20 미만인 경우 : 4단계
  - 습도가 20 이상 30 미만인 경우 : 3단계
  - 습도가 30 이상 40 미만인 경우 : 2단계
  - 습도가 40 이상 50 미만인 경우 : 1단계
  - 습도가 50 이상인 경우 : 0단계
- "target" 모드
  - 습도가 설정값 미만일 경우 : 3단계
  - 습도가 설정값 이상일 경우 : 1단계
- "minimum"모드
  - 습도가 설정값 미만일 경우 : 1단계
  - 습도가 설정값 이상일 경우 : 0단계
  
상우가 설정한 가습기의 모드를 나타낸 문자열 `mode_type`, 현재 공기 중 습도를 나타낸 정수 `humidity`, 설정값을 나타낸 정수 `val_set`이 주어질 때 현재 가습기가 몇 단계로 작동 중인지 return하도록 빈칸을 채워 solution 함수를 완성해 주세요.

## 제한사항
- `mode_type`은 "auto", "target", "minimum" 세 가지 중 하나의 값을 갖습니다.
- 0 ≤ `humidity`, `val_set` ≤ 100

## 입출력 예
|mode_type|	humidity|	val_set|	result|
|---|---|---|---|
|"auto"|	23|	45|	3|
|"target"|	41|	40|	1|
|"minimum"|	10|	34|	1|

## 입출력 예 설명
### 입출력 예 #1
- "auto"모드이므로 습도에 따라 가습량이 조절됩니다. 현재 습도가 20 이상 30 미만이므로 3을 return합니다.
### 입출력 예 #2
- "target"모드이고, 설정값보다 습도가 높으므로 1을 return합니다.
### 입출력 예 #3
- "minimum"모드이고, 설정값보다 습도가 낮으므로 1을 return합니다.

## solution.py
```python
# mode_type : target
def func1(humidity, val_set):
    if humidity < val_set:
        return 3
    return 1

# mode_type : auto
def func2(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4    
    else:
        return 5

# mode_type : minimum
def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 0

# main
def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2(humidity)
    elif mode_type == "target":
        answer = func1(humidity, val_set)
    elif mode_type == "minimum":
        answer = func3(humidity, val_set)
    return answer
```

## 해설
1. 각 `func`가 어떤 모드에 대한 동작을 하는지 파악하는 것이 관건이다.
2. `func1(humidity, val_set)`은 **humidity < val_set일 때 3을 return** 하므로 `target 모드`일 때의 작동을 정의한 함수이다.
3. `func2(humidity)`는 **0~5단계별 return 값이 정의**되어 있으므로 `auto모드`의 함수이다.
4. `func3(humidity, val_set)`은 **humidity < val_set일 때 1을 return** 하므로 `minimum 모드`일 때의 작동을 정의한 함수이다.
5. 각 함수의 동작을 잘 파악하여 `mode_type`에 따라 `answer`의 값을 설정해준다.