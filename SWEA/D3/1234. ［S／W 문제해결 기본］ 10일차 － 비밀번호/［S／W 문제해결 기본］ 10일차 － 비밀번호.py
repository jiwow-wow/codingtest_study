T = 10
for tc in range(1,T+1):
    N,s = input().split()
    l = list(s)
    

    stack =[]
    for c in l:
        stack.append(c)

        if len(stack) >= 2:
            if stack[-2] == stack[-1]:
                stack.pop()
                stack.pop()
    print(f"#{tc} {''.join(map(str, stack))}")

