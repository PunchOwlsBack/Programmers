def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:    # 가채점 점수와 실제 점수가 같은지 확인
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer