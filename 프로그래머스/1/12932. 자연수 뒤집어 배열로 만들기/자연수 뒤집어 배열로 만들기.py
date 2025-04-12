def solution(n):
    n_str = str(n)

    reversed_str = n_str[::-1] 

    result = []

    for i in reversed_str:
        result.append(int(i)) 

    return result
