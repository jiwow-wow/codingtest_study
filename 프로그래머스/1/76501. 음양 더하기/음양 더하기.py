def solution(absolutes, signs):
    answer =[ a if (signs[i]==1) else -a for i,a in enumerate(absolutes)  ]
    return sum(answer)