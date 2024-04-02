def solution(plans):
    from collections import deque
    answer = []
    recon_plan = []
    for plan in plans:
        lecture, start_time, running_time = plan
        start_time = int(start_time.split(':')[0])*60 + int(start_time.split(':')[1])
        running_time = int(running_time)
        recon_plan.append([lecture, start_time, running_time])


    recon_plan.sort(key=lambda x:x[1])
    recon_plan = deque(recon_plan)
    

    # print(recon_plan)

    stack = []
    while recon_plan:
        cur_lec, cur_st, cur_rt = recon_plan.popleft()
        
        if recon_plan:
            next_lec, next_st, next_rt = recon_plan[0]
            

            if cur_st + cur_rt > next_st:
                stack.append([cur_lec, cur_st, cur_rt-(next_st-cur_st)])
                continue
            else:
                print(cur_lec)
                answer.append(cur_lec)
            
            vacant = next_st - (cur_st+cur_rt)
            while vacant and stack:
                if stack and vacant >= stack[-1][2]:
                    vacant -= stack[-1][2]
                    lec,_,_=stack.pop()
                    print(lec)
                    answer.append(lec)
                if stack and vacant < stack[-1][2]:
                    stack[-1][2] -= vacant
                    break


        else:
            print(cur_lec)
            answer.append(cur_lec)
    
    while stack:
        lec,_,_ = stack.pop()
        print(lec)
        answer.append(lec)

    return answer