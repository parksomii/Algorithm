def solution(num, total):
    for start in range(-1000, 1000):
        seq = [start + i for i in range(num)]
        if sum(seq) == total:
            return seq
