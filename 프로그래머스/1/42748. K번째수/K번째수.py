def solution(array, commands):
    answer = []
    for c in commands:
        sorted_arr = sorted(array[ c[0]-1: c[1]  ])
        answer.append(sorted_arr[c[2] -1])
    return answer

"""
return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

"""