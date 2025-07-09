def solution(code):
    mode = 0  # 시작 모드는 0
    ret = ''  # 결과 문자열

    for idx in range(len(code)):
        char = code[idx]
        if char == '1':
            mode = 1 - mode  # 모드 전환 (0 <-> 1)
        else:
            if mode == 0 and idx % 2 == 0:
                ret += char
            elif mode == 1 and idx % 2 == 1:
                ret += char

    return ret if ret else "EMPTY"