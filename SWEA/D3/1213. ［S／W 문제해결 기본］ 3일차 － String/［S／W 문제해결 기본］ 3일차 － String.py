# count() 말고 리스트로 풀기

for test_case in range(1,11):
    _ = input()
    target_str = input()
    text = input()
    
    cnt =0
    for i in range(0, len(text) - len(target_str)+1 ): # idx = 0~len(text)-  
        
        if text[i:i + len(target_str)] == target_str:
            cnt += 1
    print(f"#{test_case} {cnt}")