def solution(friends, gifts):
    answer = 0
    gift = {name:[0,0] for name in friends}
    next_gift = {name:0 for name in friends}
    record = {a:{b:0 for b in friends if b != a} for a in friends}
    
    for g in gifts:
        g = g.split(" ")
        gift[g[0]][0] += 1 # 준 선물
        gift[g[1]][1] += 1 # 받은 선물
        record[g[0]][g[1]] += 1
        
    # 선물 지수
    gift_index = {g:gift[g][0] - gift[g][1] for g in gift}
    
    # 다음달 계산    
    for i in range(len(friends)):
        for j in range(i+1,len(friends)):
            f1,f2 = friends[i],friends[j]
            if record[f1][f2] > record[f2][f1]:
                next_gift[f1] += 1
            elif record[f1][f2] < record[f2][f1]:
                next_gift[f2] += 1
            else:
                if gift_index[f1] > gift_index[f2]:
                    next_gift[f1] += 1
                elif gift_index[f1] < gift_index[f2]:
                    next_gift[f2] += 1
    return max(next_gift.values())