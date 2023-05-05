import numpy as np

from core.utils.convert_dict_to_lists import convert_dict_to_lists
from core.utils.is_out_of_bounds import is_out_of_bounds
from models.new_new_model import function
from visual.plotter import Plotter
from visual.values import scale, grid, markers, colors


def run1():
    skip_range = range(1, 10000 + 1)
    time_range = range(1, 1000 + 1)
    x_start = 0.88
    y_start = 0.17
    α = 1
    β = 0.3962
    p_range = np.arange(0, 0.11, 0.001)

    f = lambda p, x, y: function.__x(α, β, p, x, y)
    g = lambda p, x, y: function.__y(α, β, p, x, y)

    values_x = dict()
    values_y = dict()

    upper_bound = 10_000
    lower_bound = 0

    x_0 = x_start
    y_0 = y_start
    for p in p_range:
        values_x[p] = []
        values_y[p] = []

        for _ in skip_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(y_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(y_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    source_x = convert_dict_to_lists(values_x)
    source_y = convert_dict_to_lists(values_y)

    path = "C:\\Users\\lkora\\Desktop\\2x.txt"
    with open(path, 'w') as f:
        for i in range(len(source_x[0])):
            line = str(source_x[0][i]) + " " + str(source_x[1][i]) + "\n"
            f.write(line)

    path = "C:\\Users\\lkora\\Desktop\\2y.txt"
    with open(path, 'w') as f:
        for i in range(len(source_y[0])):
            line = str(source_y[0][i]) + " " + str(source_y[1][i]) + "\n"
            f.write(line)

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('x', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_x[0], source_x[1], markers.nothing, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('y', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_y[0], source_y[1], markers.nothing, colors.steel_blue)
     .show_last())


def run2():
    skip_range = range(1, 1000 + 1)
    time_range = range(1, 1000 + 1)
    x_start = 0.88
    y_start = 0.17
    α = 1
    β = 0.3962
    p_range = np.arange(0.0, 1.0, 0.001)

    f = lambda p, x, y: function.__x(α, β, p, x, y)
    g = lambda p, x, y: function.__y(α, β, p, x, y)

    values_x = dict()
    values_y = dict()

    upper_bound = 10_000
    lower_bound = 0

    x_0 = x_start
    y_0 = y_start
    for p in p_range:
        values_x[p] = []
        values_y[p] = []

        for _ in skip_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, x_0, y_0)
            y_t = g(p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    source_x = convert_dict_to_lists(values_x)
    source_y = convert_dict_to_lists(values_y)

    path = "C:\\Users\\lkora\\Desktop\\3x.txt"
    with open(path, 'w') as f:
        for i in range(len(source_x[0])):
            line = str(source_x[0][i]) + " " + str(source_x[1][i]) + "\n"
            f.write(line)

    path = "C:\\Users\\lkora\\Desktop\\3y.txt"
    with open(path, 'w') as f:
        for i in range(len(source_y[0])):
            line = str(source_y[0][i]) + " " + str(source_y[1][i]) + "\n"
            f.write(line)

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('x', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_x[0], source_x[1], markers.nothing, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('y', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_y[0], source_y[1], markers.nothing, colors.steel_blue)
     .show_last())


def run3():
    skip_range = range(1, 1000 + 1)
    time_range = range(1, 1000 + 1)
    x_start = 0.88
    y_start = 0.17
    α = 1
    # β = 0.3962
    p_range = np.arange(0.0, 1.0, 0.001)

    f = lambda β, p, x, y: function.__x(α, β, p, x, y)
    g = lambda β, p, x, y: function.__y(α, β, p, x, y)

    values_x = dict()
    values_y = dict()

    upper_bound = 10_000
    lower_bound = 0

    x_0 = x_start
    y_0 = y_start
    for p in p_range:
        values_x[p] = []
        values_y[p] = []

        β = 1552/8881 * (p + (186501/77600))
        for _ in skip_range:
            x_t = f(β, p, x_0, y_0)
            y_t = g(β, p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(β, p, x_0, y_0)
            y_t = g(β, p, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    source_x = convert_dict_to_lists(values_x)
    source_y = convert_dict_to_lists(values_y)

    path = "C:\\Users\\lkora\\Desktop\\3x.txt"
    with open(path, 'w') as f:
        for i in range(len(source_x[0])):
            line = str(source_x[0][i]) + " " + str(source_x[1][i]) + "\n"
            f.write(line)

    path = "C:\\Users\\lkora\\Desktop\\3y.txt"
    with open(path, 'w') as f:
        for i in range(len(source_y[0])):
            line = str(source_y[0][i]) + " " + str(source_y[1][i]) + "\n"
            f.write(line)

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('x', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_x[0], source_x[1], markers.nothing, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('y', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_y[0], source_y[1], markers.nothing, colors.steel_blue)
     .show_last())


def run4():
    skip_range = range(1, 1000 + 1)
    time_range = range(1, 1000 + 1)
    x_start = 0.88
    y_start = 0.17
    α = 1
    # β = 0.3962
    p_range = np.arange(0.42, 0.7, 0.001)

    f = lambda β, p, x, y: function.__x(α, β, p, x, y)
    g = lambda β, p, x, y: function.__y(α, β, p, x, y)

    values_x = dict()
    values_y = dict()

    upper_bound = 10_000
    lower_bound = 0

    x_0 = x_start
    y_0 = y_start
    for p in p_range:
        values_x[p] = []
        values_y[p] = []

        σ = 8881/1552 * p - 186501/77600
        for _ in skip_range:
            x_t = f(p, σ, x_0, y_0)
            y_t = g(p, σ, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, σ, x_0, y_0)
            y_t = g(p, σ, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    source_x = convert_dict_to_lists(values_x)
    source_y = convert_dict_to_lists(values_y)

    path = "C:\\Users\\lkora\\Desktop\\3x.txt"
    with open(path, 'w') as f:
        for i in range(len(source_x[0])):
            line = str(source_x[0][i]) + " " + str(source_x[1][i]) + "\n"
            f.write(line)

    path = "C:\\Users\\lkora\\Desktop\\3y.txt"
    with open(path, 'w') as f:
        for i in range(len(source_y[0])):
            line = str(source_y[0][i]) + " " + str(source_y[1][i]) + "\n"
            f.write(line)

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('x', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_x[0], source_x[1], markers.nothing, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('y', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_y[0], source_y[1], markers.nothing, colors.steel_blue)
     .show_last())


def run5():
    skip_range = range(1, 1000 + 1)
    time_range = range(1, 1000 + 1)
    x_start = 0.88
    y_start = 0.17
    α = 1
    # β = 0.3962
    p_range = np.arange(0.42, 0.7, 0.001)

    f = lambda β, p, x, y: function.__x(α, β, p, x, y)
    g = lambda β, p, x, y: function.__y(α, β, p, x, y)

    values_x = dict()
    values_y = dict()

    upper_bound = 10_000
    lower_bound = 0

    x_0 = x_start
    y_0 = y_start
    for p in p_range:
        values_x[p] = []
        values_y[p] = []

        σ = 8881/1552 * p - 186501/77600
        for _ in skip_range:
            x_t = f(p, σ, x_0, y_0)
            y_t = g(p, σ, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
        for _ in time_range:
            x_t = f(p, σ, x_0, y_0)
            y_t = g(p, σ, x_0, y_0)
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            if is_out_of_bounds(x_t, upper_bound, lower_bound):
                break
            x_0 = x_t
            y_0 = y_t
            values_x[p].append(x_t)
            values_y[p].append(y_t)

    source_x = convert_dict_to_lists(values_x)
    source_y = convert_dict_to_lists(values_y)

    path = "C:\\Users\\lkora\\Desktop\\3x.txt"
    with open(path, 'w') as f:
        for i in range(len(source_x[0])):
            line = str(source_x[0][i]) + " " + str(source_x[1][i]) + "\n"
            f.write(line)

    path = "C:\\Users\\lkora\\Desktop\\3y.txt"
    with open(path, 'w') as f:
        for i in range(len(source_y[0])):
            line = str(source_y[0][i]) + " " + str(source_y[1][i]) + "\n"
            f.write(line)

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('x', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_x[0], source_x[1], markers.nothing, colors.steel_blue)
     .show())

    (Plotter()
     .setup_x_label('$\\gamma$')
     .setup_y_label('y', label_pad=5)
     # .setup_y_scale(scale.linear)
     .setup_y_scale(scale.linear)
     .setup_grid(grid.major)
     .setup_title('Bifurcation')
     .scatter(source_y[0], source_y[1], markers.nothing, colors.steel_blue)
     .show_last())