def solution(survey, choices):
    score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3} # 번호:점수
    result = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    answer = ''
    
    def type(a,b):
        if result[a] >= result[b]:
            return a
        else:
            return b
        
    for s,c in zip(survey,choices):
        dag, ag = s[0],s[1]
        if c <= 4:
            result[dag] += score[c]
        else:
            result[ag] += score[c]
    
    answer += type('R','T')
    answer += type('C','F')
    answer += type('J','M')
    answer += type('A','N')
    return answer