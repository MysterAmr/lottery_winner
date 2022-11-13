#k = number of allowed operations
def winner(lotteryID, winnerID, k):
    s = ''
    subs = ''
    for i in range(k):
        if lotteryID[i] == winnerID[i]:
            s += lotteryID[i]
        else:
            if ord(winnerID[i]) > ord(lotteryID[i]):
                s += chr(ord(lotteryID[i])+1)
            else:
                s += chr(ord(lotteryID[i])-1)
                
    for i in s:
        if i in winnerID:
            subs += i
        
    return len(subs)
