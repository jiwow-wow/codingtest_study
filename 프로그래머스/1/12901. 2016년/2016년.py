def solution(a, b):
    week_list = ["FRI","SAT","SUN","MON","TUE","WED", "THU"]
    month_day_list= [31,29,31,30,31,30,31,31,30,31,30,31]
    
    day = sum(month_day_list[:a-1]) + b -1
    
    return week_list[(day % 7)]