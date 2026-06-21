"""
프로그래머스 Lv.0 (기초 14일차-4)

풀이날짜: 2026-06-21
문제번호: 181884
문제명: n보다 커질 떄까지 더하기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181884

학습내용:
- next(iter, 기본값) : 반복자에서 다음 값을 하나 꺼내오는 함수 

"""
def solution(numbers, n):
    answer = 0

    for num in numbers:
        if  answer > n:
                break
        answer += num
    
    return answer