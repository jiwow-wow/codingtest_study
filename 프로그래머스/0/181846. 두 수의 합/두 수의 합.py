# def solution(a, b):
#     return str(int(a) + int(b))
"""
해당 풀이가 불가능한 이유(gpt):
Python 3.11부터는 보안상의 이유(CVE-2020-10735)로 너무 긴 문자열을 int()로 변환하는 것을 제한합니다.

"""

def solution(a, b):
    result = []
    carry = 0

    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        num1 = int(a[i]) if i >= 0 else 0
        num2 = int(b[j]) if j >= 0 else 0

        total = num1 + num2 + carry
        result.append(str(total % 10))
        carry = total // 10

        i -= 1
        j -= 1

    return ''.join(result[::-1])