# [PCCE 기출문제] 1번 / 문자 출력
## 문제 설명
주어진 코드는 변수에 데이터를 저장하고 출력하는 코드입니다. 아래와 같이 출력되도록 빈칸을 채워 코드를 완성해 주세요.

## 출력 예시
```python
3
2
1
Let's go!
```

## solution.py
```python
message = "Let's go!"

print("3\n2\n1")
print(message)
```

## 해설
1. Python에서 줄바꿈은 `\n`을 이용한다.
   ```python
   print("3\n2\n1")
   ```
   
2. `print(message)`는 `message`의 값을 출력하는 함수이다. 출력 예시에 맞게 `Let's go!` 라는 값을 `message`에 할당한다.
   
   ```python
   message = "Let's go!"
   ```