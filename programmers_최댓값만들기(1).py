def solution(numbers):
    numbers = sorted(numbers)
    num_len = len(numbers)
    answer = 0
    answer = numbers[num_len-1] * numbers[num_len-2]
    
    return answer