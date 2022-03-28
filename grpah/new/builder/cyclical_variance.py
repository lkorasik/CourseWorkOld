import statistics

from new.algorithms.bifurcation import bifurcation
from new.builder.variance import variance


def cyclical_variance(time_range, x_start, b_range, f, count):
    draw_x = []
    for b in b_range:
        draw_x.append(b)

    data = []
    for i in range(count):
        values = bifurcation(time_range, x_start, b_range, f,
                             down_border=None)
        draw_y = variance(b_range, values)[1]
        data.append(draw_y)

    length = len(data[0])
    result = []
    for i in range(length):
        arr = []
        for item in data:
            arr.append(item[i])
        result.append(statistics.variance(arr))

    return draw_x, result
