import re

def solution(new_id):
    
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    new_id = re.sub(r"\.+", '.', new_id)
    new_id = re.sub(r'^\.|\.$', '', new_id)
    new_id = 'a' if new_id == '' else new_id
    new_id = new_id[:15]
    new_id = new_id.strip('.')
    while(len(new_id) < 3):
        new_id += new_id[-1]
    
    return new_id
    

#     answer = ''
#     new_id = new_id.lower()

#     for c in new_id:
#         if c.islower() or c.isdigit() or c in ['-', '_', '.']:
#             answer += c
#     new_id = answer
    
#     new_id = re.sub(r'\.+', '.', new_id )
#     new_id = new_id.strip('.')
    
#     if len(new_id) == 0:
#         new_id = 'a'
#     if len(new_id) >= 16:
#         new_id = new_id[:15]
#         new_id = new_id.rstrip('.')
#     while (len(new_id) <3):
#         new_id += new_id[-1]
            
#     return new_id