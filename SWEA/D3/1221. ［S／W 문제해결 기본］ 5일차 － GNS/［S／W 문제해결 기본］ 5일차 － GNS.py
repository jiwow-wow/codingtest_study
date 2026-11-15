T = int(input())

a_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
a_dic = {}
for i, s in enumerate(a_num):
    a_dic[s] = 0

for test_case in range(1, 11):
    print(f"#{test_case}")
    _, length = input().split(" ")
    length = int(length)
    anum_list = list(input().split(" "))
    #print(anum_list)
    
    for key, val in a_dic.items():
        a_dic[key]  = anum_list.count(key)
        #print(anum_list.count(key)) 
    #print(a_dic)
    
    for key, val in a_dic.items():
        for _ in range(val):
            print(f"{key}", end = " ")
        
