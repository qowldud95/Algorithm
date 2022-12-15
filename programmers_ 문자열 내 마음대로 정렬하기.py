from collections import defaultdict
def solution(strings, n):
    answer = []
    
    #사전정렬 먼저 해주어야함. 같은 문자열이 여럿일 경우, 사전순으로 앞쪽에 위치해야 하기 때문.
    strings = sorted(strings)
    
    x = defaultdict(int)
    
    for i in range(len(strings)):
        x[i] = strings[i][n]   #0:u, 1:e, 2:a
    
    #defaultdict 정렬
    sorted_dict = sorted(x.items(), key=lambda item:item[1]) 
    print(sorted_dict) #[(1, 'a'), (0, 'e'), (2, 'u')]
    
    #index 차례대로 answer 에 넣기 
    for i in range(len(sorted_dict)):
        answer.append(strings[sorted_dict[i][0]])

    return answer