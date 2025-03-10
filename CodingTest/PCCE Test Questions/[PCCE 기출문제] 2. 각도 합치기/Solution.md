# [PCCE 기출문제] 2번 / 각도 합치기
## 문제 설명
일반적으로 두 선분이 이루는 각도는 한 바퀴를 360도로 하여 표현합니다. 따라서 각도에 360의 배수를 더하거나 빼더라도 같은 각을 의미합니다. 예를 들면, 30도와 390도는 같은 각도입니다.

주어진 코드는 각도를 나타내는 두 정수 `angle1`과 `angle2`가 주어질 때, 이 두 각의 합을 0도 이상 360도 미만으로 출력하는 코드입니다. 코드가 올바르게 작동하도록 한 줄을 수정해 주세요.

## 제한사항
- 0 ≤ `angle1` ≤ 5000
- 0 ≤ `angle2` ≤ 5000

## 입출력 예
### 입력 #1
```python
280
485
```
### 출력 #1
```python
45
```

## 입출력 예 설명
### 입출력 예 #1
`angle1`과 `angle2`의 합은 765도이고, 765를 720을 빼면 45도이므로 45를 출력합니다.

## solution.py
```python
angle1 = int(input())
angle2 = int(input())

sum_angle = (angle1 + angle2) % 360
print(sum_angle)
```

## 해설
1. 입력 받은 두 각(`angle1`, `angle2`)의 합을 나머지 연산자인 `%` 을 이용하여 360으로 나누어 그 나머지 값을 구한다.
   
```python
(angle1 + angle2) % 360
```