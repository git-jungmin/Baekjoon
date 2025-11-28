def solution(new_id):
    vaild = 'abcdefghijklmnopqrstuvwxyz0123456789-._'
    new_id = new_id.lower()
    new_id = ''.join(c for c in new_id if c in vaild)
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    new_id = new_id.strip('.')
    print(new_id)
    if not new_id:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    while new_id and len(new_id) <= 2:
        new_id += new_id[-1]
    new_id = new_id.strip('.')
    print(new_id)
    return new_id