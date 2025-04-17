def solution(quiz):
    answer = []
    for q in quiz:
        x, op, y, eq, z = q.split()
        x, y, z = int(x), int(y), int(z)
        
        if op == '+':
            result = x + y
        else:
            result = x - y
        
        if result == z:
            answer.append("O")
        else:
            answer.append("X")
    
    return answer
