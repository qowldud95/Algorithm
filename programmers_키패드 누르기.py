def solution(numbers, hand):
    leftSpot = '*' #왼 엄지 위치
    rightSpot = '#' #오른 엄지 위치
    answer = ''
    
    keypad = { 1: [0,0], 2: [1,0], 3: [2,0],
               4: [0,1], 5: [1,1], 6: [2,1],
               7: [0,2], 8: [1,2], 9: [2,2],
               "x": [0,3], 0: [1,3], "#":[2,3], }
    
    for i in numbers:
        if i in [1,4,7] :
            answer += 'L'
            leftSpot = i
        elif i in [3,6,9] :
            answer += 'R'
            rightSpot = i
        elif i in [2,5,8,0] :
            curPos = keypad[i]
            leftPos = keypad[leftSpot]
            rightPos = keypad[rightSpot]
            
            leftDistance = abs(curPos[0]-leftPos[0]) + abs(curPos[1]-leftPos[1])
            rightDistance = abs(curPos[0]-rightPos[0]) + abs(curPos[1]-rightPos[1])
            
            if leftDistance > rightDistance :
                answer += 'R'
                rightSpot = i
            elif leftDistance < rightDistance :
                answer += 'L'
                leftSpot = i
            else :
                if hand == 'left':
                    answer += 'L'
                    leftSpot = i
                else :
                    answer += 'R'
                    rightSpot=i
    return answer