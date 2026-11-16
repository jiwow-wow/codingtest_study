T = int(input())

for t in range(1,T+1):
    N = int(input())
    nums = list(map( int, input().split()))
    
    tree = [0]
    for n in nums:
        tree.append(n)
        cur = len(tree) -1
        while cur > 1 and tree[cur] < tree[cur//2]:
            tree[cur], tree[cur//2] = tree[cur//2], tree[cur]
            cur = cur //2
            
    sum_tree =0
    i = (len(tree) -1)//2
    while (i  > 0):
        sum_tree += tree[i]
        i = i//2
    print(f"#{t} {sum_tree}")
    