def solution(common):
    
    diff = common[1] - common[0]
    
    if common[2] - common[1] == diff:
        return common[-1] + diff
    else:
        ratio = common[1] // common[0]
        return common[-1] * ratio
