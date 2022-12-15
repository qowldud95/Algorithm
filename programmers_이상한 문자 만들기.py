def solution(s):
    answer=''
    answer_list = s.split(' ')
    answer_list_len = len(answer_list)
    
    for i in range(answer_list_len) :
        for j in range(len(answer_list[i])) :
            if j%2 == 0 :
                answer += answer_list[i][j].upper()
            else :
                answer += answer_list[i][j].lower()
        if i == answer_list_len-1 :
            break
        answer += ' '
    return answer