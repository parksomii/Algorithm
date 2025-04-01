def solution(a, b):
    ab = int(str(a) + str(b))
    ba = int(a * b * 2 )
    return max(ab, ba)
