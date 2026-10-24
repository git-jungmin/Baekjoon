import math
def solution(players, m, k):
    answer = 0
    server = [1 for i in range(24)]
    for i in range(24):
        if players[i] >= (m * server[i]):
            add = ((players[i] - (m * server[i])) // m) + 1
            answer += add
            for j in range(i,min(24,i+k)):
                server[j] += add
            print(answer)
            print(server)
    return answer