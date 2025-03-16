from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    dq = deque([])
    total_weight = 0
    while truck_weights or dq:
        answer += 1
        if dq and dq[0][1] == answer:
            total_weight -= dq.popleft() [0]
        if truck_weights and truck_weights[0] + total_weight <= weight:
            truck = truck_weights.pop(0)
            dq.append((truck, answer + bridge_length))
            total_weight += truck
    return answer