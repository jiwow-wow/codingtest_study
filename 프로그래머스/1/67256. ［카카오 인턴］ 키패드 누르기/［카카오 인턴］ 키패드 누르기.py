def solution(numbers, hand):
    answer = ''
    
    num_list = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
    L_list = [10]
    R_list = [12]
    
    for n in numbers:
        if n in [1,4,7]:
            L_list.append(n)
            answer += 'L'
            
        elif n in [3,6,9]:
            R_list.append(n)
            answer += 'R'
            
        else: 
            if n == 0:
                n =11
            x = (n-1) // 3 
            y = (n-1) % 3
            
            L_distance = abs((L_list[-1] -1)//3 - x) + abs((L_list[-1] -1) %3 -y)
            R_distance = abs((R_list[-1] -1)//3 - x) + abs((R_list[-1] -1) %3 -y)
            
            if L_distance > R_distance:
                R_list.append(n)
                answer += 'R'
            elif L_distance < R_distance:
                L_list.append(n)
                answer += 'L'
            else: 
                if hand =="right":
                    R_list.append(n)
                    answer += 'R'
                else:
                    L_list.append(n)
                    answer += 'L'
    return answer