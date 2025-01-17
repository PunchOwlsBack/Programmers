# 지폐 90도 회전
def swap(bill):
    bill[0], bill[1] = bill[1], bill[0]
    return bill

# 돌렸을 때 지갑에 들어가는지 체크
def checkFitWhenSwapBill(wallet, bill):
    bill = swap(bill)
    if(wallet[0] >= bill[0] & wallet[1] >= bill[1]):
        return 1
    else:
        return 0

# return bigger Value in size
def getBiggerValue(size):
    bigger = size[0]
    if(bigger > size[1]):
        return bigger
    else:
        return size[1]
    
# return smaller value in size
def getSmallerValue(size):
    smaller = size[0]
    if(smaller < size[1]):
        return smaller
    else:
        return size[1]
    
# 지갑에 안들어가는 상황인지 체크
def checkFit(wallet, bill):
    big_bill = getBiggerValue(bill)
    sml_bill = getSmallerValue(bill)
    
    big_wallet = getBiggerValue(wallet)
    sml_wallet = getSmallerValue(wallet)
    
    if(sml_bill > sml_wallet & big_bill > big_wallet):
        return 1
    else:
        return 0

# mainActivity
def mainActivity(wallet, bill, count):
    if(checkFitWhenSwapBill == 1):
        return count
    else:
        big_val = getBiggerValue(bill)
        sml_val = getSmallerValue(bill)
    
        while(checkFit(wallet, bill) == 0):
            if(bill[0] > bill[1]):
                bill[0] //= 2
            else:
                bill[1] //= 2
            count += 1
        
        return count
        

def solution(wallet, bill):
    answer = 0
    answer = mainActivity(wallet, bill, answer)
    return answer