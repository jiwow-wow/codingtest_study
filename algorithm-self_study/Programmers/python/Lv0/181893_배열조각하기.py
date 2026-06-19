"""
프로그래머스 Lv.0 (기초 12일차-5)

풀이날짜: 2026-06-19
문제번호: 181893
문제명: 배열조각하기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181893

학습내용:
- 처음 for 문에서 for k, q in enumerate(query):를 사용하면 query[i]대신 q로 사용가능

"""

def solution(arr, query):
    
    for i in range(len(query)):
        if i%2==0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]

    return arr