def solution(s):
    result = []
    words = s.split(' ')
    for word in words:
        new_word = ''
        for i, char in enumerate(word):
            if i % 2 == 0:
                new_word += char.upper()
            else:
                new_word += char.lower()
        result.append(new_word)
    return ' '.join(result)
