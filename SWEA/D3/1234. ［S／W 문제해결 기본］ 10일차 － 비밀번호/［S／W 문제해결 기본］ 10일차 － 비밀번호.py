for tc in range(1,11):
    n, pw =  input().split(" ")
    pwl = list(pw)
    stack = [ ]
    for c in pwl:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    print(f"#{tc} {''.join(stack)}")
        
    