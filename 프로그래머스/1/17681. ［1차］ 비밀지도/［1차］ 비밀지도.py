def solution(n, arr1, arr2):
    answer = []
    b_list =[]
    
    for a1, a2 in zip(arr1, arr2):
        # b_list.append( bin(a1 | a2)[2:].zfill(n) )
        b_list.append( bin(a1 | a2)[2:].rjust(n, '0') )

        
    for b in b_list:
        answer.append(b.replace('1', '#').replace("0", ' ') )
                
    return answer

"""
.rjust(n, 'a') 함수 => 전체 길이를 n으로 만들고 빈곳을 'a' 로 채우기

  for i in range(n):
        a = str(bin(arr1[i]|arr2[i])[2:]).rjust(n,'0').replace('1','#').replace('0',' ')
        answer.append(a)
"""