def solution(today, terms, privacies):
    answer = []
    terms_dict = {}

    ty, tm, td = map(int, today.split("."))
    
    for t in terms: 
        opt, month = t.split(" ")
        terms_dict[opt] = int(month)
        
    for i,p in enumerate(privacies):
        date, opt =p.split(" ")
        year, month, day = map(int, date.split('.'))
        
        month += terms_dict[opt]
        
        year += (month - 1) // 12
        month = (month - 1) % 12 + 1
            
        day -= 1
        if day ==0: 
            day = 28
            month -= 1
            if month ==0:
                month = 12
                year -=1
        
        if (year, month, day) < (ty, tm, td):
            answer.append(i + 1)
    
        
    
    return answer