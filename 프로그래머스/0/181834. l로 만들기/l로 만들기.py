def solution(myString):
    answer = ''
    # [참일 때 값 if 조건 else 거짓일 때 값 for 변수 in 반복문]
    return     ''.join([m if m >'l' else 'l' for m in myString ])
