from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)  # 귤 크기별 개수 세기
    sorted_counts = sorted(count.values(), reverse=True)  # 개수를 내림차순 정렬
    
    total = 0  # 선택한 귤 개수
    kinds = 0  # 선택한 귤 종류 수
    
    for c in sorted_counts:
        total += c
        kinds += 1
        if total >= k:
            return kinds  # k개를 채우면 종료

    return kinds  # 일반적으로 여기 도달할 일 없음
