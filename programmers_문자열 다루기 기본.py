def solution(s):
    answer = True
    for i in range(len(s)) :
        if len(s) not in [4,6] : 
            answer = False
            break
        if s[i] not in ['0','1','2','3','4','5','6','7','8','9'] :
            answer = False
            break
    return answer