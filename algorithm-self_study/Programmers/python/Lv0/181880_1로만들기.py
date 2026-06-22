"""
프로그래머스 Lv.0 (기초 15일차-3)

풀이날짜: 2026-06-22
문제번호: 181880
문제명: 1로 만들기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181880

학습내용:
- 

"""
def solution(num_list):
    answer = 0
    
    for n in num_list:
        
        while n!=1:
            if n%2==0:
                n //=2
            else:
                n = (n-1)//2
            
            answer +=1
    return answer