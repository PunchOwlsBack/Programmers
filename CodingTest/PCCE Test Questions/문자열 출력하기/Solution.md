# 문자열 출력하기
## 문제 설명
문자열 `str`이 주어질 때, `str`을 출력하는 코드를 작성해 보세요.

## 제한사항
- 1 ≤ `str`의 길이 ≤ 1,000,000
- `str`에는 공백이 없으며, 첫째 줄에 한 줄로만 주어집니다.

## 입출력 예
### 입력 #1
```txt
HelloWorld!
```
### 출력 #1
```txt
HelloWorld!
```

## solution.py
```python
str = input()
print(str)
```

## 해설
1. 출력 함수인 print()를 이용하여 input()으로 입력받은 str의 값을 출력한다.
```python
str = input()
print(str)
```

## 여담
```python
print(input())
```
이렇게 해도 되는데, `str`이 주어졌다고 해서 그냥 정석으로 풀었다.
