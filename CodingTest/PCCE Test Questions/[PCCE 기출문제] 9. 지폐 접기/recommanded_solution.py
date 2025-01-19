def solution(wallet, bill):
    answer = 0
    
    bill = sorted(bill)
    wallet = sorted(wallet)

    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        bill[1] //= 2
        answer += 1
        bill = sorted(bill)

    return answer