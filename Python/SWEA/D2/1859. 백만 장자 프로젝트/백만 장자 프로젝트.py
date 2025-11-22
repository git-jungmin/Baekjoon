#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    test = list(map(int,input().split()))
    
    profit = 0
    max_price = 0
    
    for i in range(N-1,-1,-1):
        if test[i] > max_price:
            max_price = test[i]
        else:
            profit += max_price - test[i]
    print(f"#{test_case} {profit}")