import numpy as np


def crossing(melody_line_1, melody_line_2, crossing_type):
    cross_point = []
    while len(cross_point) < crossing_type:
        r = np.random.randint(1, len(melody_line_1)-2)
        if r not in cross_point:
            cross_point.append(r)
    cross_point.sort()

    help_point = 0
    for point in cross_point:
        melody_line_1[help_point:point], melody_line_2[help_point:point] = \
            melody_line_2[help_point:point], melody_line_1[help_point:point]
        help_point = point

    linie = [melody_line_1, melody_line_2]

    return linie[np.random.choice([0, 1])]
