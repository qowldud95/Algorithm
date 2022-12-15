def solution(n):
    answer = 0
    for j in range(1,n+1) :
        sum = 0
        for i in range(j,n+1) : 
            sum += i
            if sum == n :
                answer += 1
                break
            elif sum > n :
                break
            
    return answer