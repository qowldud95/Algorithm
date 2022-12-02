def solution(N, stages):
    userLen = len(stages)
    failRateArr = {}
    
    for i in range(1,N+1) :
        if userLen == 0 :
            failRateArr[i] =0
        else :
            failRateArr[i] = stages.count(i) / userLen
            userLen -= stages.count(i)
        
    failRateArr= sorted(failRateArr, key=lambda x : failRateArr[x], reverse=True)
    #answer = sorted(failRateArr, key=failRateArr.get, reverse=True)
    return failRateArr
