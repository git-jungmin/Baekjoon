def solution(cap, n, deliveries, pickups):
    def update(current,dist,idx):
        for i in range(idx-1,-1,-1):
            if current[i] > 0:
                current[i] -= 1
                if i > dist - 1:
                    dist = i + 1
                return current, dist, i + 1
        return current, dist, idx

    answer = 0
    idx_d,idx_p = n,n
    while True:
        dist = 0
        for c in range(cap):
            deliveries, dist, idx_d = update(deliveries,dist,idx_d)
            pickups, dist, idx_p = update(pickups,dist,idx_p)
        if dist == 0:
            break
        answer += dist * 2
    return answer