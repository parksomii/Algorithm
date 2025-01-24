import math

def solution(n):
    sqrt_n = math.isqrt(n)
    
    if sqrt_n * sqrt_n == n:
        return (sqrt_n + 1) ** 2
    else:
        return -1