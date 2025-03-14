def solution(array):
    max_count = 0
    mode = -1
    duplicate = False
    
    for num in set(array):
        count = array.count(num)
        if count > max_count:
            max_count = count
            mode = num
            duplicate = False
        elif count == max_count:
            duplicate = True
    return mode if not duplicate else -1