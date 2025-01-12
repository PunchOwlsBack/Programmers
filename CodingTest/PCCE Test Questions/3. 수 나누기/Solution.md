# [PCCE 기출문제] 3번 / 수 나누기
## 문제 설명
2자리 이상의 정수 `number`가 주어집니다. 주어진 코드는 이 수를 2자리씩 자른 뒤, 자른 수를 모두 더해서 그 합을 출력하는 코드입니다. 코드가 올바르게 작동하도록 한 줄을 수정해 주세요.

## 제한사항
- 10 ≤ `number` ≤ 2,000,000,000
- `number`의 자릿수는 2의 배수입니다.

## 입출력 예

### 입력 #1
```python
4859
```
### 출력 #1
```python
107
```
### 입력 #2
```python
29
```
### 출력 #2
```python
29
```

## solution.py
```python
number = int(input())

answer = 0

while number > 0 :
    answer += number % 100
    number //= 100

print(answer)
```

## 해설
1. `반복문`의 로직을 파악한다.
    ```python
    for i in range(1):              
        answer += number % 100      # answer = number를 100으로 나눈 후 나머지 값을 저장
        number //= 100              # number의 크기를 10^2만큼 줄임
    ```
2. 반복문 탈출 조건은 다음과 같아야 한다.
   - `number`가 더이상 **100으로 나눠지지 않아야** 한다.
   - `number`가 0보다 커야한다. 
   
   ```python
   while number > 0:
        answer += number % 100
        number //= 100
   ```

   