# Rotate a bill 90 degrees
def swap(bill):
    return [bill[1], bill[0]]

# Check if the bill fits in the wallet
def checkFit(wallet, bill):
    return bill[0] <= wallet[0] and bill[1] <= wallet[1]

# Halve the length of the large side of the bill
def resizeBill(bill):
    if bill[0] >= bill[1]:
        bill[0] //= 2
    else:
        bill[1] //= 2
        
    return bill

# Activity
def mainActivity(wallet, bill, count):
    MAX_FOLDS = 100  # Prevent infinite loop in extreme cases

    while not checkFit(wallet, bill):
        if checkFit(wallet, swap(bill)):
            break
        else:
            if count >= MAX_FOLDS: 
                return -1  # Indicate failure if folding exceeds limit
            bill = resizeBill(bill)
            count += 1
            
    return count

# main function
def solution(wallet, bill):
    answer = mainActivity(wallet, bill, 0)
    return answer