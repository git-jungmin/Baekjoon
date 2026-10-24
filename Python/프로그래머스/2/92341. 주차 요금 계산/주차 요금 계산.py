from datetime import datetime
import math

def calculate(i,o):
    in_time = datetime.strptime(i,"%H:%M")
    out_time = datetime.strptime(o, "%H:%M")
    return int((out_time - in_time).total_seconds() // 60)

def solution(fees, records):
    answer = []
    parked = {}
    tot_time = {}
    for i in records:
        t, n, r = i.split(' ')
        if r == 'IN':
            parked[n] = t
        else:
            if n in tot_time:
                tot_time[n] += calculate(parked[n],t)
            else:
                tot_time[n] = calculate(parked[n],t)
            del parked[n]
    for j in parked:
        if j in tot_time:
            tot_time[j] += calculate(parked[j],'23:59')
        else:
            tot_time[j] = calculate(parked[j],'23:59')
    for z in sorted(tot_time):
        if tot_time[z] > fees[0]:
            answer.append(fees[1] + math.ceil((tot_time[z] - fees[0]) / fees[2]) * fees[3])
        else:
            answer.append(fees[1])
    return answer