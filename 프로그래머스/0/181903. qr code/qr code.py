def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i % q == r:  # 인덱스를 q로 나눈 나머지가 r인 경우만
            answer += code[i]
    return answer
