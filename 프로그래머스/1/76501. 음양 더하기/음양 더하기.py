def solution(absolutes, signs):
    answer =[ a if (signs[i]==1) else -a for i,a in enumerate(absolutes)  ]
    return sum(answer)

"""
zip함수 사용하기
sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
"""