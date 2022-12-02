def solution(s):
    sLen = len(s)
    i = sLen//2
    
    if sLen % 2 == 0 :
        answer=s[i-1:i+1]
    else : 
        answer=s[i]
    
    return answer
