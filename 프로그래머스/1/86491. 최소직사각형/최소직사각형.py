def solution(sizes):
    answer = 0
    
    for s in sizes:
        if s[1] > s[0]:
                s[0], s[1] = s[1], s[0]
    w, h = zip(*sizes)
    
    return max(w)*max(h)