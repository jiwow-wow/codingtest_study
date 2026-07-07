def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        row = []  
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)  
        
    return answer
    # return [[c1 + c2 for c1, c2 in zip(a1, a2) ]  for a1,a2 in zip(arr1, arr2)  ]

"""
return [[c1 + c2 for c1, c2 in zip(r1, r2)] for r1, r2 in zip(arr1, arr2)]
"""