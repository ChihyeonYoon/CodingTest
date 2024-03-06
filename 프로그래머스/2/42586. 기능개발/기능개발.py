def solution(progresses, speeds):
    answer = []
    
    def work(progress, speeds):
        return [i+j for i,j in zip(progress, speeds)]
    
    while progresses:
        cnt = 0
        progresses = work(progresses, speeds)
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt +=1
        if cnt >0:
            answer.append(cnt) 

    return answer