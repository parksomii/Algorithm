def solution(arr):
    row = len(arr)
    col = len(arr[0])

    # 행이 더 많은 경우 → 각 행에 0 추가
    if row > col:
        for i in range(row):
            arr[i] += [0] * (row - col)
    # 열이 더 많은 경우 → 행을 추가
    elif col > row:
        for _ in range(col - row):
            arr.append([0] * col)

    return arr