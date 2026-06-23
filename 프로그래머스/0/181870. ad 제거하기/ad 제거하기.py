def solution(strArr):
    
    for i in range(len(strArr) - 1, -1, -1):
        if "ad" in strArr[i]:
            strArr.pop(i)
    return strArr


#뒤에서부터 조회해야 인덱스가 꼬이지 않음