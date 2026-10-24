def solution(num, total):
    answer = []
    s = total // num
    for i in range(-(num//2),(num//2)+1):
        answer.append(i+s)
        print(i)
    if num % 2 == 0:
        answer = answer[1:]
    return answer