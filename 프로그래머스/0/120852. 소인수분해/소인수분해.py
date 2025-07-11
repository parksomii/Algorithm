def solution(n):
    result = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            if divisor not in result: 
                result.append(divisor)
            n //= divisor
        else:
            divisor += 1 

    return result
