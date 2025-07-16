def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    
    answer = [sorted_emergency.index(e) + 1 for e in emergency]
    
    return answer