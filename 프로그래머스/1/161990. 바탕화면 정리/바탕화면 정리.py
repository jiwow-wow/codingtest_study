def solution(wallpaper):
    
    horizon = []
    vertical = []
    
    for i, p in enumerate(wallpaper):
                
        left = p.find('#')
        if left != -1:
            horizon.append(left)
        
        right = p.rfind('#')
        if right != -1:
            horizon.append(right)
        
        if '#' in p :
            vertical.append(i)
            
    answer= [min(vertical), min(horizon), max(vertical)+1,  max(horizon)+1]
    
    return answer