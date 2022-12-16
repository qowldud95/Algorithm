def solution(numbers):
    answer = 0
    numbers_len = len(numbers)
    
    for i in numbers :
        answer += i
    answer = round(answer / numbers_len, 1)
    return answer