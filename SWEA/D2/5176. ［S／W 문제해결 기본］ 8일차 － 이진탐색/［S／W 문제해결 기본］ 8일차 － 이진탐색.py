

def inorder(n):
    global val

    if n <= N:
        inorder(n*2)# 왼쪽
        tree[n] = val #루트

        val +=1
        inorder(n*2+1) # 오른쪽

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    val = 1
    inorder(1)
    print(f"#{tc} {tree[1]} {tree[N//2]}")