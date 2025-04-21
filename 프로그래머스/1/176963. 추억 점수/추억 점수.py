def solution(name, yearning, photo):
    answer = []

    # 1. 이름별 그리움 점수 딕셔너리로 매핑
    name_score = {}
    for i in range(len(name)):
        name_score[name[i]] = yearning[i]

    # 2. 각 사진마다 점수 합산
    for people in photo:
        total = 0
        for person in people:
            if person in name_score:
                total += name_score[person]
        answer.append(total)

    return answer
