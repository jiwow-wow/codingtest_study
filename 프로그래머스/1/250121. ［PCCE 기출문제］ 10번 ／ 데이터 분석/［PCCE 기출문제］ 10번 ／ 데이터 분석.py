def solution(data, ext, val_ext, sort_by):
    answer = []
    data_list = ["code", "date", "maximum", "remain"]
    
    for d in data:
        if d[data_list.index(ext)] <= val_ext:
            answer.append(d)
                

    answer.sort(key = lambda x: x[data_list.index(sort_by)])
    
    return answer