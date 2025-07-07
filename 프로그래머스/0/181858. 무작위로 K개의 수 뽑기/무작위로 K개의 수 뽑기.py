def solution(arr, k):
    result = []
    seen = set()  # 이미 추가된 숫자 저장

    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
            if len(result) == k:  # k개 다 모이면 중단
                break

    while len(result) < k:  # 부족하면 -1 추가
        result.append(-1)

    return result