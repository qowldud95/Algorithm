#n =1 경우의수 1    1
#n =2 경우의수 2    1,1    2
#n =3 경우의수 3    1,1,1  1,2  2,1
#n =4 경우의수 5    1,1,1,1   1,1,2    1,2,1   2,1,1  2,2
#n =5 경우의수 8    1,1,1,1,1    1,1,1,2   1,1,2,1   1,2,1,1   2,1,1,1   2,2,1,  2,1,2,                    1,2,2
#n의 경우의수는 n-1경우의수 + n-2경우의수 (피보나치수열)
#경우의수를 담을 list가 필요
#list에서 마지막 n번째에 해당하는 값 출력
#출력된 값 % 1234567 = 정답

def solution(n):
    answer = 0
    list = []
    list.append(1)
    list.append(2)
    
    for i in range(2,n) : 
        list.append(list[i-1] + list[i-2])
        
    answer = list[n-1] % 1234567
    return answer