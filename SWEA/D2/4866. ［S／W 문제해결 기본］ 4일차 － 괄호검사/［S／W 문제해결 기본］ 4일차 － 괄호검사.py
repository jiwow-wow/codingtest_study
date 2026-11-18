

T = int(input())

for tc in range(1, T +1):
    l_str = list(input())
    m_l = ["{", "}", "[", "]", "(", ")"]

    stack =[]
    for c in l_str:
        if c in m_l:
            stack.append(c)

            if len(stack) >= 2 and stack[-2] == m_l[m_l.index(stack[-1])-1]:
                stack.pop()
                stack.pop()

    print(f"#{tc}", end =" ")
    if len(stack) == 0:
        print(1)
    else:
        print(0)

