def solution(ingredient):
    temp=[]
    answer =0
    for i in range(len(ingredient)):
            temp.append(ingredient[i])
            if temp[-4:] == [1,2,3,1]:
                answer+=1
                for k in range(4) :
                    temp.pop()
    return answer 
