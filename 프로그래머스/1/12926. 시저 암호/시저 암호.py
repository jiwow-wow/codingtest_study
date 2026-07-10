
def solution(s, n):
    answer = ''
    
    for c in s:
        if c.islower():
            answer += chr(((ord(c) -ord('a') +n) % 26) + 97)
        elif c.isupper():
            answer+= chr(((ord(c) - ord("A")+n) % 26) +65)
        else:
            answer += ' '
    return answer 