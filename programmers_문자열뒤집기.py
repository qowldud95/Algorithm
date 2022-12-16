def solution(my_string):
    answer = ''
    my_string_len = len(my_string) -1
    for i in range(len(my_string)) : 
        answer += my_string[my_string_len - i]
    return answer