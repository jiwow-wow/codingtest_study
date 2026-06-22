"""
프로그래머스 Lv.0 (기초 12일차-1)

문제번호: 181897
문제명: 리스트 자르기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181897

학습내용:
쿼리(n) 종류가 많아지면 2분할 방식으로 2이하, 3이상 으로 만들어주면(2진트리) 
n:1~4까지 어떤 경우든 조건문 2번 안에 자리를 찾아 들어가게 된다
"""

def solution(n, slicer, num_list):
    answer = []
    
    if n == 1:
        return num_list[0:slicer[1]+1]
    elif n ==2:
        return num_list[slicer[0]:]
    elif n ==3: 
        return num_list[slicer[0]:slicer[1]+1]
    elif n==4:
        return num_list[slicer[0]:slicer[1]+1:slicer[2]]


'''
다른 사람의 풀이

a, b, c = slicer
    return [num_list[:b + 1], num_list[a:], num_list[a:b + 1], num_list[a:b + 1:c]][n - 1]

'''