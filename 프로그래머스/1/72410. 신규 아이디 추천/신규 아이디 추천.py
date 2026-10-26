import re

def solution(new_id):

    answer = ''
    new_id = new_id.lower()

    for c in new_id:
        if c.islower() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    new_id = answer
    
    new_id = re.sub(r'\.+', '.', new_id )
    new_id = new_id.strip('.')
    
    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    elif len(new_id) <= 2:
        while (len(new_id) <3):
            new_id += new_id[-1]
            
    return new_id