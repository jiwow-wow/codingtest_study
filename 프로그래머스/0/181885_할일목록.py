"""
프로그래머스 Lv.0 (기초 14일차-3)

풀이날짜: 2026-06-21
문제번호: 181885
문제명: 할일목록
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181885

학습내용:
- map, zip 사용하면 더 빠르게 생성가능

"""

def solution(todo_list, finished):
    answer = []
    
    for i,t in enumerate(todo_list):
        if not finished[i]:
            answer.append(t)
        
    return answer

'''
최적 풀이:
return list(compress(todo_list, map(lambda x: x^1, finished)))
return [x for x, b in zip(todo_list, finished) if not b]
'''

