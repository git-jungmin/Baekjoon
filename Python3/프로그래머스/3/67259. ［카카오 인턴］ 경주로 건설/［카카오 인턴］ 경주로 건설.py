import heapq
INF = int(1e9)

def solution(board):
    n = len(board)
    
    costs = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    
    for i in range(4):
        costs[0][0][i] = 0
    
    # 다음 이동 방향 (위,왼쪽,아래,오른쪽)
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    # 이전 방향 (위,왼쪽,아래,오른쪽)
    dz = [0,1,2,3]
    
    heap = []
    
    # heap 초기화 (d,x,y,z)
    if board[1][0] == 0:
        heapq.heappush(heap, (100,1,0,2))
        costs[1][0][2] = 100
    if board[0][1] == 0:
        heapq.heappush(heap, (100,0,1,3))
        costs[0][1][3] = 100
    
    while heap:
        c,x,y,d = heapq.heappop(heap)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny]:
                continue
            
            nc = c + (100 if i == d else 600)
            
            if costs[nx][ny][d] > nc:
                heapq.heappush(heap, (nc,nx,ny,i))
                costs[nx][ny][d] = nc
    
    return min(costs[n-1][n-1])