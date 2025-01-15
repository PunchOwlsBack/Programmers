def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    while(len(answer) < 4):     # 닉네임 길이가 4 미만일 때, o를 길이가 4가 될 때까지 이이붙임 
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer