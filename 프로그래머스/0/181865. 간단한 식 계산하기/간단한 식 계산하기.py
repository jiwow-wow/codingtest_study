def solution(binomial):
    answer = 0
    
    return eval(binomial)

# 하지만 eval()은 보안상 취약함, 다른 풀이 최적은 다음과 같음
# def solution(binomial):
#     a, op, b = binomial.split()

#     a = int(a)
#     b = int(b)

#     operations = {
#         "+": a + b,
#         "-": a - b,
#         "*": a * b
#     }

#     return operations[op]