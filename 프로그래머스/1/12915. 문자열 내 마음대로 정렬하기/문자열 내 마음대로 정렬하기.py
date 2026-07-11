def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
"""
다중조건 정렬:
정렬의 첫번째 기준을 x[n] 으로 하고, 두번째 기준으로 문자열 전체 x 를 기준으로 정렬한다
"""