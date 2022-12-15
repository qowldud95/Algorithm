from collections import defaultdict
def solution(survey, choices):
    answer = ''
    
    #검사지선택지 testSelect
    testSelect = defaultdict(int)
    testSelect[1] = 3
    testSelect[2] = 2
    testSelect[3] = 1
    testSelect[4] = 0
    testSelect[5] = -1
    testSelect[6] = -2
    testSelect[7] = -3
    
    #각 캐릭터별 점수를 담을 score
    score = defaultdict(int)
    
    #각 캐릭터별 점수 구하는 로직
    for i in range(len(survey)) :
        if(testSelect[choices[i]] < 0) :
            user = survey[i][1]
            score[user] += abs(testSelect[choices[i]])
        elif(testSelect[choices[i]] > 0) :
            user = survey[i][0]
            score[user] += testSelect[choices[i]]
    
    #문제에서 제시된 지표        
    zipyo = ['R','T'],['C','F'],['J','M'], ['A','N']
    
    #각 지표에 대하여 높은점수를 가진 캐릭터 뽑기
    #점수가 같으면 알파벳 순서로 결정
    for i in zipyo :
        if(score[i[0]] > score[i[1]]) :
            max_user = i[0]
            answer += max_user
        elif(score[i[0]] < score[i[1]]) :
            max_user=i[1]
            answer += max_user
        else :
            temp = [i[0], i[1]]
            temp.sort()
            max_user = temp[0]
            answer += max_user
    
    return answer