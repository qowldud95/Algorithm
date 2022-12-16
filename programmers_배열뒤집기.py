def solution(num_list):
    answer = []
    num_list_len = len(num_list) -1
    
    for i in range(len(num_list)) :
        answer.append(num_list[num_list_len-i])
    return answer