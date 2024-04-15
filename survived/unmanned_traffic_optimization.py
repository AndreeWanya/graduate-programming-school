def traffic_light_checking(time: int, track: list) -> int:
    red_green = [0]
    n = track[0] + track[1]
    while sum(red_green) < n:
        red_green.append(red_green[-1] + track[1])
        red_green.append(red_green[-1] + track[2])
    for i in range(0, len(red_green), 2):
        if time in range(red_green[i], track[1]):
            return track[1] - time
    return 0

def Unmanned(L: int, N: int, track: list) -> int:
    time = track[0][0]
    lenght = track[0][0]
    for i in range(1, N):
        check_if_green = traffic_light_checking(time, track[i-1])
        if check_if_green == 0:
            time += track[i][0] - track[i-1][0]
        else:
            time += track[i][0] - track[i-1][0] + check_if_green
        lenght += track[i][0] - track[i-1][0]
    if traffic_light_checking(time, track[i]) == 0:
        time += L - lenght
    else:
        time += L - lenght + traffic_light_checking(time, track[i])
    return time

#print(Unmanned(10, 2, [[3, 5, 5], [5, 2, 2]]))