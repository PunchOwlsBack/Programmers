# [PCCE 기출문제] 1번 / 출력
## 문제 설명
주어진 초기 코드는 변수에 데이터를 저장하고 출력하는 코드입니다. 아래와 같이 출력되도록 빈칸을 채워 코드를 완성해 주세요.

## 출력 예시
```txt
Spring is beginning
13
310
```

## solution.py
```python
string_msg = "Spring is beginning"  # string형
int_val = 3                         # int형 
string_val = "3"                    # string형

print(string_msg)
print(int_val + 10)
print(string_val + "10")
```

## 해설
1. `string_msg`에 저장된 문장을 그대로 출력해야 한다. `string_msg`를 `"Spring is beginning"`로 초기화해준다.
2. i`nt_val`에 `10`을 더해 `13`을 출력해야 한다. `int_val`은 `int형` 변수이므로 `3`으로 초기화한다.
3. `string_val`에 `"10"` 이라는 문자열을 붙여 출력해야 한다. `310`을 만들기 위해서 `string_val`을 "3"으로 초기화한다.
