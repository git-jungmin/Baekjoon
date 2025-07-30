from collections import defaultdict
def solution(genres, plays):
    best = []
    genre_play_count = defaultdict(int) # 장르 별 총 재생 횟수
    genre_songs = defaultdict(list)
    for i,(g,p) in enumerate(zip(genres,plays)):
        genre_play_count[g] += p
        genre_songs[g] += [(i,p)]
    for g in sorted(genre_play_count, key = lambda x : genre_play_count[x], reverse = True):
        sorted_songs = sorted(genre_songs[g], key = lambda y : y[1] ,reverse = True)
        best.append(sorted_songs[0][0])
        if len(sorted_songs) >= 2:
            best.append(sorted_songs[1][0])
    return best