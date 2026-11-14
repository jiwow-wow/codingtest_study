for test_case in range(1, 11):
    dump = int(input())
    boxs = list( map( int, input().split()  ) )
    #print(boxs)
    #is_flatten = False
    
    for i in range(dump):
        idx_max, idx_min = boxs.index(max(boxs)), boxs.index(min(boxs))
        if idx_max == idx_min:
            break
        else:
            boxs[idx_max] -= 1
            boxs[idx_min] += 1
    max_minus_min = max(boxs) - min(boxs)
    print(f"#{test_case} {max_minus_min}")

