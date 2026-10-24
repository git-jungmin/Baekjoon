def solution(numbers, hand):
    answer = ''
    phone = {'1':(1,1), '2':(1,2), '3':(1,3), '4':(2,1), '5':(2,2), '6':(2,3), '7':(3,1), '8':(3,2), '9':(3,3), '*':(4,1), '0':(4,2), '#':(4,3)}
    l,r = '*','#'
    for i in numbers:
        i = str(i)
        if i in ('1','4','7'):
            answer += 'L'
            l = i
        elif i in ('3','6','9'):
            answer += 'R'
            r = i
        else:
            l_dist = abs(phone[i][0] - phone[l][0]) + abs(phone[i][1] - phone[l][1])
            r_dist = abs(phone[i][0] - phone[r][0]) + abs(phone[i][1] - phone[r][1])
            if l_dist < r_dist:
                l = str(i)
                answer += 'L'
            elif r_dist < l_dist:
                r = str(i)
                answer += 'R'
            else:
                if hand == 'right':
                    r = str(i)
                    answer += 'R'
                else:
                    l = str(i)
                    answer += 'L'
    return answer
