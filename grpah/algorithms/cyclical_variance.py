import statistics

from algorithms.bifurcation import bifurcation
from algorithms.variance import variance
from visual.line import Line


def cyclical_variance(time_range, x_start, b_range, f, count):
    line = Line()
    for b in b_range:
        line.add_x(b)

    data = []
    for i in range(count):
        values = bifurcation(time_range, x_start, b_range, f, down_border=None)
        variance_ = variance(b_range, values).y
        data.append(variance_)

    for i in range(len(data[0])):
        arr = []
        for item in data:
            arr.append(item[i])
        line.add_y(statistics.variance(arr))

    return line