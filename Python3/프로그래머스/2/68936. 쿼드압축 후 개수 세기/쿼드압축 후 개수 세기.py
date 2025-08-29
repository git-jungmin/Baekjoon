def solution(arr):
    answer = []
    size = len(arr)
    def compress(x,y,size):
        first = arr[x][y]
        for i in range(x,x+size):
            for j in range(y,y+size):
                if arr[i][j] != first:
                    half = size//2
                    c1 = compress(x,y,half)
                    c2 = compress(x,y+half,half)
                    c3 = compress(x+half,y,half)
                    c4 = compress(x+half,y+half,half)
                    return [c1[0]+c2[0]+c3[0]+c4[0], c1[1]+c2[1]+c3[1]+c4[1]]
        if first == 0:
            return [1,0]
        else:
            return [0,1]
    return compress(0,0,size)