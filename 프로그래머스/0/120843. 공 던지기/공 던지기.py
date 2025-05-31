def solution(numbers, k):
    
    n = len(numbers)
    
    index = (2 * (k - 1)) % n
    
    return numbers[index]
