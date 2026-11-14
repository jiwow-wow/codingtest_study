for test_case in range(1, 11):
    dump = int(input())
    boxs = list( map( int, input().split()  ) )
    #print(boxs)
    #is_flatten = False
    
    for i in range(dump):
        max_box, min_box = max(boxs), min(boxs)
        idx_max, idx_min = boxs.index(max_box), boxs.index(min_box)
        
        if (max_box - min_box) <= 1:
            break
        else:
            boxs[idx_max] -= 1
            boxs[idx_min] += 1
    max_minus_min = max(boxs) - min(boxs)
    print(f"#{test_case} {max_minus_min}")

