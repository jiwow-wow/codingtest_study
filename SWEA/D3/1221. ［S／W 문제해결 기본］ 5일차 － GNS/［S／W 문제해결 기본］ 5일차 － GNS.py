T = int(input())

a_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
a_dic = {}
for i, s in enumerate(a_num):
    a_dic[s] = i
#print(a_dic)

for test_case in range(1, 11):
    print(f"#{test_case}")
    
    _, length = input().split(" ")
    length = int(length)
    anum_list = input().split()
    count = [0]* 10
    
    for s in anum_list:
        count[a_dic[s]] += 1
    #print(count)
    
    for key, val in a_dic.items():
        for _ in range(count[val]):
            print(key, end = " ")
        
