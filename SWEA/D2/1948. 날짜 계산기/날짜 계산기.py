T = int(input())
# T = 10

cal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1,T+1):
    l = list(map( int , input().strip().split(" ")))

    m1,d1,m2,d2 = l[0], l[1], l[2], l[3]
    res = 0

    if m1 == m2:
        res = d2 - d1 + 1
    else:
        res  = sum(cal[m1+1:m2]) + cal[m1] - d1+d2+1
    print(f"#{tc} {res}")


