while True:
    N, A, B = map(int, input().split())
    if N == A == B == 0:
        break

    teams = [list(map(int, input().split())) for _ in range(N)]
    teams.sort(key=lambda x: abs(x[1] - x[2]), reverse=True)  # A와 B의 거리 차이가 큰 순으로 정렬

    total_distance = 0
    equal_distance_teams = []  # A, B 거리가 같은 팀

    # 거리 차이가 있는 팀들 처리
    for balloons, dist_a, dist_b in teams:
        if dist_a > dist_b:  # B가 더 가까운 경우
            if B >= balloons:
                B -= balloons  # B의 풍선 사용
                total_distance += dist_b * balloons
            else:
                total_distance += dist_b * B
                balloons -= B
                total_distance += dist_a * balloons
                B = 0
        elif dist_a < dist_b:  # A가 더 가까운 경우
            if A >= balloons:
                A -= balloons
                total_distance += dist_a * balloons
            else:
                total_distance += dist_a * A
                balloons -= A
                total_distance += dist_b * balloons
                A = 0
        else:
            equal_distance_teams.append([balloons, dist_a, dist_b])

    # 거리가 같은 팀들 처리
    for balloons, dist, _ in equal_distance_teams:
        total_distance += balloons * dist

    print(total_distance)
