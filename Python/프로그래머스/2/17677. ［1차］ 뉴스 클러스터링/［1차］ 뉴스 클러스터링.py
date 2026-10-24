from collections import Counter
def extract_alpha(s):
    return [s[i:i+2].lower() for i in range(len(s)-1) if s[i:i+2].isalpha()]

def solution(str1, str2):
    a = extract_alpha(str1)
    b = extract_alpha(str2)
    counter_a = Counter(a)
    counter_b = Counter(b)
    intersection = counter_a & counter_b
    union = counter_a | counter_b
    if not union:
        return 65536
    return int((sum(intersection.values()) / sum(union.values())) * 65536)