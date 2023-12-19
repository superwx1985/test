def get_number_of_dropped_packets(requests, max_packets, rate):
    left = 0
    lost = 0
    t_dict = dict()
    for r in requests:
        t_dict[r[0]] = r[1]

    t = 0
    while t_dict:
        if t in t_dict:
            data = t_dict.pop(t)
            left = data + left
            print(t, "add > {}".format(data))
        print(t, "start", left, lost)

        if left > max_packets:
            current_lost = left - max_packets
            lost = lost + current_lost
            left = max_packets
            print(t, "lost > {}".format(current_lost))

        left = left - rate
        if left < 0:
            left = 0
        print(t, "end", left, lost)
        t += 1
    return lost


if __name__ == '__main__':

    _requests = [[1, 8]
        , [4, 9], [6, 7]]
    _max_packets = 8
    _rate = 3
    result = get_number_of_dropped_packets(_requests, _max_packets, _rate)
    print("lost", result)

