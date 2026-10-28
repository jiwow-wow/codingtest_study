from collections import Counter

def solution(k, tangerine):
    answer =0
    counts = Counter(tangerine)
    
    # for cost, val in counts.most_common():
    for key, val in sorted(counts.items(), key = lambda x: x[1] , reverse =True):
        k -=  val
        answer += 1
        if k <= 0:
            break
    
    return answer
    
#     answer = 1
#     t_dic = {}
    
#     for i in set(tangerine):
#         t_dic[i] = tangerine.count(i)
    
#     sorted_dic = dict(sorted( t_dic.items(), key =  lambda x: x[1], reverse= True))
    
#     for key, val in sorted_dic.items():
#         k -= val
#         if k > 0:
#             answer +=1
#         else:
#             break        
    # return answer