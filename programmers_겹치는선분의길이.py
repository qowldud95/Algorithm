def solution(lines): 
    answer = 0
    x = dict()
    xx =[]
    
    for i in lines :
        for j in i :
            xx.append(j)
    xx = sorted(xx)
    
    for i in range(xx[0],xx[-1]) :
        x[i] = 0
        
    for i in lines :
        for j in range(i[0],i[1]) :
            x[j] += 1
    
    for i in range(xx[0],xx[-1]) :
        if x[i] >= 2 :
            answer +=1
            
    return answer