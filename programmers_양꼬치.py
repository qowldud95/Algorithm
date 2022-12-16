def solution(n, k):
    answer = 0
    yang_pay = 12000 * n
    drink_pay = 2000 * k
    
    service = int(n / 10)
    drink_pay = drink_pay - (2000*service)
    
    answer = yang_pay + drink_pay
    return answer