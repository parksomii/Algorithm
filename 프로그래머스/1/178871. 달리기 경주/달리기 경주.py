def solution(players, callings):
    # 선수 이름별 현재 등수 저장
    player_to_index = {}
    for i in range(len(players)):
        player_to_index[players[i]] = i

    # 호출된 선수 이름 하나씩 처리
    for call in callings:
        # 현재 불린 선수의 등수 찾기
        current_idx = player_to_index[call]

        # 앞에 있는 선수 찾기
        front_player = players[current_idx - 1]

        # 불린 선수와 앞선수의 위치 바꾸기
        players[current_idx - 1], players[current_idx] = players[current_idx], players[current_idx - 1]

        # 딕셔너리에도 바뀐 위치를 반영
        player_to_index[call] = current_idx - 1
        player_to_index[front_player] = current_idx

    return players
