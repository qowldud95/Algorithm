def solution(a, b):
    answer = ''
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    sum = 0
    for i in range(a-1) :
        print(i)
        sum += day[i]
    sum += b
    
    answer = week[(sum % 7)-1]
    return answer