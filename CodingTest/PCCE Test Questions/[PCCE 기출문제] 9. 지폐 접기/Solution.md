# [PCCE 기출문제] 9번 / 지폐 접기
## 문제 설명
민수는 다양한 지폐를 수집하는 취미를 가지고 있습니다. 지폐마다 크기가 달라 지갑에 넣으려면 여러 번 접어서 넣어야 합니다. 예를 들어 지갑의 크기가 30 * 15이고 지폐의 크기가 26 * 17이라면 한번 반으로 접어 13 * 17 크기로 만든 뒤 90도 돌려서 지갑에 넣을 수 있습니다. 지폐를 접을 때는 다음과 같은 규칙을 지킵니다.

지폐를 접을 때는 항상 길이가 긴 쪽을 반으로 접습니다.
접기 전 길이가 홀수였다면 접은 후 소수점 이하는 버립니다.
접힌 지폐를 그대로 또는 90도 돌려서 지갑에 넣을 수 있다면 그만 접습니다.
지갑의 가로, 세로 크기를 담은 정수 리스트 `wallet`과 지폐의 가로, 세로 크기를 담은 정수 리스트 `bill`가 주어질 때, 지갑에 넣기 위해서 지폐를 최소 몇 번 접어야 하는지 return하도록 solution함수를 완성해 주세요.

지폐를 지갑에 넣기 위해 접어야 하는 최소 횟수를 구하는 과정은 다음과 같습니다.

```txt
1. 지폐를 접은 횟수를 저장할 정수 변수 answer를 만들고 0을 저장합니다.
2. 반복문을 이용해 bill의 작은 값이 wallet의 작은 값 보다 크거나 bill의 큰 값이 wallet의 큰 값 보다 큰 동안 아래 과정을 반복합니다.
    2-1. bill[0]이 bill[1]보다 크다면
        bill[0]을 2로 나누고 나머지는 버립니다.
    2-2. 그렇지 않다면
        bill[1]을 2로 나누고 나머지는 버립니다.
    2-3. answer을 1 증가시킵니다.
3. answer을 return합니다.
```
- 위의 의사코드와 작동방식이 다른 코드를 작성해도 상관없습니다.

## 제한사항
- `wallet`의 길이 = `bill`의 길이 = 2
- 10 ≤ `wallet[0]`, `wallet[1]` ≤ 100
- 10 ≤ `bill[0]`, `bill[1]` ≤ 2,000

## 입출력 예
|wallet	|bill	|result|
|---|---|---|
|[30, 15]	|[26, 17]|	1|
|[50, 50]|	[100, 241]|	4|

## 입출력 예 설명
### 입출력 예 #1
- 지문과 동일합니다.
### 입출력 예 #2
- 지폐를 접으면 다음과 같이 크기가 줄어듭니다. 따라서 4번 접으면 지갑에 넣을 수 있습니다.
- [100, 241] -> [100, 120] -> [100, 60] -> [50, 60] -> [50, 30]
---
- cpp를 응시하는 경우 리스트는 배열과 동일한 의미이니 풀이에 참고해주세요.
  - ex) 번호가 담긴 정수 리스트 numbers가 주어집니다. => 번호가 담긴 정수 배열 numbers가 주어집니다.
- java를 응시하는 경우 리스트는 배열, 함수는 메소드와 동일한 의미이니 풀이에 참고해주세요.
  - ex) solution 함수가 올바르게 작동하도록 한 줄을 수정해 주세요. => solution 메소드가 올바르게 작동하도록 한 줄을 수정해 주세요.
  
## solution.py
```python
def solution(wallet, bill):
    answer = 0
    
    bill = sorted(bill)
    wallet = sorted(wallet)

    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        bill[1] //= 2
        answer += 1
        bill = sorted(bill)

    return answer
```

## 해설
1. wallet과 bill을 각각 sorted 함수를 이용하여 정렬 후, 문제 설명에 나와 있는 반복문의 로직을 그대로 사용한다. 
2. 이때, 이미 bill을 정렬했기 때문에 bill의 대수를 비교하는 로직은 빼고, 가장 큰 수를 1/2 하는 경우만 사용한다.
   ```python
   while bill[0] > wallet[0] or bill[1] > wallet[1]:
        bill[1] //= 2
        answer += 1
   ```
3. 한 번 접은 후, 지폐를 90도 돌렸을 때 지갑이 들어가는 경우를 살펴보기 위해 `bill`을 다시 `sorted`로 정렬한다. 이 작업은 반복문이 끝날때까지 실행된다.
   ```python
   while bill[0] > wallet[0] or bill[1] > wallet[1]:
        bill[1] //= 2
        answer += 1

        bill = sorted(bill)     # 지폐를 90도 돌림
   ```

## 시행착오
`sorted()` 함수를 몰라서 `swap()`과 `대수비교 함수`를 따로 만들어서 굉장히 긴 코드를 작성했다. 1/2하는 함수도 따로 만들어서 사용하였는데, 막상 정답을 확인하니 그럴 필요가 없어서 좀 뻘쭘했다...

`java`에 익숙해서 while이나 if문에 `괄호()`를 무조건 사용해야 하는 줄 알았다. `python`의 기본 구문을 좀 더 공부할 필요를 느꼈다.

아래는 초기에 내가 작성한 코드이다.

```python
# Rotate a bill 90 degrees
def swap(bill):
    return [bill[1], bill[0]]

# Check if the bill fits in the wallet
def checkFit(wallet, bill):
    return bill[0] <= wallet[0] and bill[1] <= wallet[1]

# Halve the length of the large side of the bill
def resizeBill(bill):
    if bill[0] >= bill[1]:
        bill[0] //= 2
    else:
        bill[1] //= 2
        
    return bill

# Activity
def mainActivity(wallet, bill, count):
    MAX_FOLDS = 100  # Prevent infinite loop in extreme cases

    while not checkFit(wallet, bill):
        if checkFit(wallet, swap(bill)):
            break
        else:
            if count >= MAX_FOLDS: 
                return -1  # Indicate failure if folding exceeds limit
            bill = resizeBill(bill)
            count += 1
            
    return count

# main function
def solution(wallet, bill):
    answer = mainActivity(wallet, bill, 0)
    return answer
```