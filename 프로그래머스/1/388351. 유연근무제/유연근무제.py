def solution(schedules, timelogs, startday):
    answer = []
    for i, time_list in enumerate(timelogs):
        for j,t in enumerate(time_list):
            day = (startday + j - 1) % 7 + 1
            
            if day == 6 or day == 7:
                day +=1 
                continue
                
            admit_time = schedules[i] +10
            if admit_time %100 >= 60: 
                admit_time = admit_time//100*100 + 100 + admit_time%100 % 60
                
                print(admit_time)
            if t > admit_time:
                answer.append(i)
                # print(day, t,  schedules[i]+10, admit_time)
                day +=1 
                
            else: 
                day +=1
        
    print(answer)    
    return len(schedules) - len(set(answer))