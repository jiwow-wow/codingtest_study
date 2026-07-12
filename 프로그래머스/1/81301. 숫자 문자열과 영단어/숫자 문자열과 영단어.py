def solution(s):
    answer = 0
    string_list = ["zero", "one", "two", "three", 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    # if string_list in s:
    for st in string_list:
        s = s.replace(st, str(string_list.index(st)))
    return int(s)