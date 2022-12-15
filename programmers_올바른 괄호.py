def solution(s):
    answer = True
    stack = []
    for i in range(len(s)) :        
        if(s[0] == ')' or s[-1] == '(') :
            answer = False
            break
            
        stack.append(s[i])
        
        if s[i] == ')' :
            if len(stack) == 1 :
                answer = False
                break
            else :
                stack.pop()
                stack.pop()
            
    if len(stack) != 0 :
        answer = False
        
    return answer