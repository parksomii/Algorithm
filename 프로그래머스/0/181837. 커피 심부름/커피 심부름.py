def solution(order):
    total = 0
    for menu in order:
        if "cafelatte" in menu:
            total += 5000
        else:
            total += 4500
    return total