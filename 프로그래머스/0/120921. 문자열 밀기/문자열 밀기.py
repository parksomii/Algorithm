def solution(A, B):
    for i in range(len(A)):
        if A == B:
            return i
        A = A[-1] + A[:-1]  # 오른쪽으로 한 칸 밀기
    return -1
