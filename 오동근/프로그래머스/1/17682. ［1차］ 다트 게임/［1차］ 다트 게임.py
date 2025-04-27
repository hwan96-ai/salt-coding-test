def solution(dartResult):
    dartResult = dartResult.replace('10', 'X')
    dartList = list(dartResult)
    score = []
    for i in range(len(dartList)):
        if dartList[i] == 'X':
            dartList[i] = 10
    
    for i in range(len(dartList)):
        if dartList[i] == 'S':
            score.append(int(dartList[i-1]) ** 1)
        elif dartList[i] == 'D':
            score.append(int(dartList[i-1]) ** 2)
        elif dartList[i] == 'T':
            score.append(int(dartList[i-1]) ** 3)
        
        if dartResult[i] == "*":
            if len(score)>=2 :
                score[-2] *= 2
                score[-1] *= 2
            else:
                score[-1] *= 2
        elif dartResult[i] == "#":
            score[-1] *= -1
        
    answer = sum(score)
    return answer