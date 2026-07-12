def solution(s):
    answer = 0
    string_list = ["zero", "one", "two", "three", 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for st in string_list:
        s = s.replace(st, str(string_list.index(st)))
    return int(s)


"""
딕셔너리를 활용한 풀이:

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
"""