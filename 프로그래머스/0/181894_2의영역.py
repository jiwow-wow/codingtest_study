"""
프로그래머스 Lv.0 (기초 12일차-4)

풀이날짜: 2026-06-19
문제번호: 181894
문제명: 2의영역
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181894

학습내용:
- cnt 말고 if 2 not in arr 사용하면 좋음
- arr[::-1].index(2) 사용하면 맨 뒤에 있는 2의 인덱스 찾기 가능

"""

def solution(arr):
    answer = []
    arr2 =[]
    
    cnt = arr.count(2)
    if cnt == 0: 
        answer.append(-1)
    elif cnt == 1:
        answer = [2]
    elif cnt >=2:
        for i in range(len(arr)):
            if arr[i] ==2:
                arr2.append(i)
        print(arr2)
        answer.extend(arr[min(arr2):max(arr2)+1])
    return answer

""" 고수의 풀이
def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]
"""