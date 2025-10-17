def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        row = arr1[i] | arr2[i]
        binary = bin(row)[2:].zfill(n)
        line = binary.replace('1', '#').replace('0', ' ')
        answer.append(line)

    return answer