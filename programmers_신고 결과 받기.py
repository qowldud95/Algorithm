from collections import defaultdict
def solution(id_list, report, k):
    report = list(set(report))
    cnt = defaultdict(int)
    user = defaultdict(set)
    answer = []
    for i in report :
        a,b = i.split(" ")
        cnt[b] += 1
        user[a].add(b)
        
    for i in id_list :
        result = 0
        for j in user[i] :
            if cnt[j] >= k :
                result += 1
        answer.append(result)
    return answer