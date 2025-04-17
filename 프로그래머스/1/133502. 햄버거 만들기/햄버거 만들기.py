def solution(ingredient):
    answer = 0
    stack = []

    for i in ingredient:
        stack.append(i)

        # 스택 길이가 최소 4이고, 마지막 4개가 햄버거 조합일 때
        if stack[-4:] == [1, 2, 3, 1]:
            # 포장하고 재료 제거
            del stack[-4:]
            answer += 1

    return answer
