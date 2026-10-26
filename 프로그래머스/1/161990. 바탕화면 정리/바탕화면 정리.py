def solution(wallpaper):
    
    left_list = [] 
    right_list = []
    vertical = []
    
    for i, p in enumerate(wallpaper):
                
        left = p.find('#')
        left_list.append(left if left >= 0 else 999)
        
        right = p.rfind('#')
        right_list.append(right)
        
        if '#' in p :
            vertical.append(i)
            
    answer= [min(vertical), min(left_list), max(vertical)+1,  max(right_list)+1]
    
    return answer