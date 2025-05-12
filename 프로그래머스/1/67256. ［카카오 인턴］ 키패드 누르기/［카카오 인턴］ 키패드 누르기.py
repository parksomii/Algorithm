def solution(numbers, hand):
    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    left = keypad['*']
    right = keypad['#']
    
    result = ''

    for num in numbers:
        pos = keypad[num]

        if num in [1, 4, 7]:
            result += 'L'
            left = pos

        elif num in [3, 6, 9]:
            result += 'R'
            right = pos

        else:
            left_dist = abs(left[0] - pos[0]) + abs(left[1] - pos[1])
            right_dist = abs(right[0] - pos[0]) + abs(right[1] - pos[1])

            if left_dist < right_dist:
                result += 'L'
                left = pos
            elif left_dist > right_dist:
                result += 'R'
                right = pos
            else:
                if hand == 'right':
                    result += 'R'
                    right = pos
                else:
                    result += 'L'
                    left = pos

    return result