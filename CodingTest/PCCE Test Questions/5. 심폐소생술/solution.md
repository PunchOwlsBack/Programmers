# [PCCE 기출문제] 5번 / 심폐소생술
## 문제 설명
심폐소생술은 다음과 같은 순서를 통해 실시합니다.

1. 심정지 및 무호흡 확인 [check]
2. 도움 및 119 신고 요청 [call]
3. 가슴압박 30회 시행 [pressure]
4. 인공호흡 2회 시행 [respiration]
5. 가슴압박, 인공호흡 반복 [repeat]

주어진 solution 함수는 심폐소생술을 하는 방법의 순서가 담긴 문자열들이 무작위 순서로 담긴 리스트 `cpr`이 주어질 때 각각의 방법이 몇 번째 단계인지 순서대로 담아 return하는 함수입니다. solution 함수가 올바르게 작동하도록 빈칸을 채워 solution 함수를 완성해 주세요.

## 제한사항
- `cpr`은 다음 문자열들이 한 번씩 포함되어 있습니다.
    - "check", "call", "pressure", "respiration", "repeat"

## 입출력 예
| cpr	| result|
|-------|-------|
|["call", "respiration", "repeat", "check", "pressure"]	|[2, 4, 5, 1, 3]|
["respiration", "repeat", "check", "pressure", "call"]|[4, 5, 1, 3, 2]|

### 입출력 예 #1
- "call", "respiration", "repeat", "check", "pressure"은 각각 2, 4, 5, 1, 3 번째 순서이므로 [2, 4, 5, 1, 3]을 리턴합니다.
### 입출력 예 #2
- "respiration", "repeat", "check", "pressure", "call"은 각각 4, 5, 1, 3, 2 번째 순서이므로 [4, 5, 1, 3, 2]를 리턴합니다.
---
- cpp를 응시하는 경우 리스트는 배열과 동일한 의미이니 풀이에 참고해주세요.
    - ex) 번호가 담긴 정수 리스트 `numbers`가 주어집니다. 
      - 번호가 담긴 정수 배열 `numbers`가 주어집니다.
- java를 응시하는 경우 리스트는 배열, 함수는 메소드와 동일한 의미이니 풀이에 참고해주세요.
    - ex) solution 함수가 올바르게 작동하도록 한 줄을 수정해 주세요. 
      - solution 메소드가 올바르게 작동하도록 한 줄을 수정해 주세요.
  
## solution.py
```python
def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr: 
        for i in range(5):
            if action == basic_order[i]: # 같은 값이라면
                answer.append(i+1) # 동일값 위치+1 저장
    return answer
```

## 해설
1. 이중 for문을 사용하여 해결하는 문제이다.
2. 리스트 `cpr`의 모든 **elememt**마다 `basic_order`의 값과 비교하여 같은 값일 때의 위치를 구한다.
3. 이 때, 해당 위치는 `배열의 index`이므로, **1을 더해준다**.
