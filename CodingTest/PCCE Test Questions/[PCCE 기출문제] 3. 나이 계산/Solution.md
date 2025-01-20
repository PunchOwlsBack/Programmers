# [PCCE 기출문제] 3번 / 나이 계산
## 문제 설명
나이를 세는 방법은 여러 가지가 있습니다. 그중 한국식 나이는 태어난 순간 1살이 되며 해가 바뀔 때마다 1살씩 더 먹게 됩니다. 연 나이는 태어난 순간 0살이며 해가 바뀔 때마다 1살씩 더 먹게 됩니다. 각각 나이의 계산법은 다음과 같습니다.

- 한국식 나이 : 현재 연도 - 출생 연도 + 1
- 연 나이 : 현재 연도 - 출생 연도

출생 연도를 나타내는 정수 `year`와 구하려는 나이의 종류를 나타내는 문자열 `age_type`이 주어질 때 2030년에 몇 살인지 출력하도록 빈칸을 채워 코드를 완성해 주세요. `age_type`이 "Korea"라면 한국식 나이를, "Year"라면 연 나이를 출력합니다.

## 제한사항
- 1950 ≤ `year` ≤ 2030
- `age_type`은 "Korea" 또는 "Year"만 주어집니다.

## 입출력 예
### 입력 #1
```txt
2000
Korea
```
### 출력 #1
```txt
31
```
### 입력 #2
```txt
1999
Year
```

### 출력 #2
```txt
31
```

## solution.py
```python
year = int(input())
age_type = input()

if age_type == "Korea":
    answer = 2030-year+1
elif age_type == "Year":   
    answer = 2030-year

print(answer)
```

## 해설
1. 나이의 종류(`age_type`)가 한국식 나이(`Korea`)일 때의 2030년에서의 나이(`answer`)는 현재 연도(`2030`) - 출생 연도(`year`) + `1`이다.
   
   ```python
    if age_type == "Korea":
    answer = 2030-year+1
   ```

2.  나이의 종류(`age_type`)가 연 나이(`Year`)일 때의 2030년에서의 나이(`answer`)는 현재 연도(`2030`) - 출생 연도(`year`)이다.
   
    ```python
    elif age_type == "Year":   
    answer = 2030-year
    ```