def solution(brown, yellow):
    total = brown + yellow  # 전체 타일 개수
    
    for h in range(1, int(total**0.5) + 1):  # 가능한 높이(h)를 탐색
        if total % h == 0:  # h가 total의 약수라면
            w = total // h  # 너비 계산
            if (w - 2) * (h - 2) == yellow:  # 노란색 타일 개수 검증
                return [w, h]  # 가로, 세로 반환
