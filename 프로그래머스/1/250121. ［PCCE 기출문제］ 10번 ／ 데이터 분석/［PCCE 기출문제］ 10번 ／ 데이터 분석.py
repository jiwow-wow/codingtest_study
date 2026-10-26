def solution(data, ext, val_ext, sort_by):
    answer = []
    sort_list = ["code", "date", "maximum", "remain"]
    ext_list = ["code","date","maximum","remain"]
    
    for d in data:
        if d[ext_list.index(ext)] <= val_ext:
            answer.append(d)
                

    answer.sort(key = lambda x: x[sort_list.index(sort_by)])
    
    return answer