def solution(wallet, bill):
    answer = 0
    while min(wallet) < min(bill) or max(wallet) < max(bill):
        bill = [max(bill)//2,min(bill)]
        answer += 1
    return answer