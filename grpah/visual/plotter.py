from matplotlib import pyplot as plt

from visual.line import Line


class Plotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self._legend = dict()

    def _setup(self, x_label, y_label, y_scale, grid, title):
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.yscale(y_scale)
        self.ax.grid(which=grid)
        plt.title(title)
        self.fig.canvas.manager.set_window_title(title)
        return self

    def setup_title(self, title):
        plt.title(title)
        self.fig.canvas.manager.set_window_title(title)
        return self

    def setup_grid(self, grid):
        self.ax.grid(which=grid)
        return self

    def setup_y_scale(self, scale):
        plt.yscale(scale)
        return self

    def setup_x_scale(self, scale):
        plt.xscale(scale)
        return self

    def adjust(self, left=0.125, bottom=0.11, right=0.9, top=0.88, w_space=0.2, h_space=0.2):
        plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=w_space, hspace=h_space)
        return self

    def setup_x_ticks(self, font_size=10, rotation=0):
        plt.xticks(fontsize=font_size, rotation=rotation)
        return self

    def setup_x_label(self, label, rotation=0, font_size=10, label_pad=0, location='center'):
        # plt.xticks(fontsize=14, rotation=90)
        plt.xlabel(label, rotation=rotation, fontsize=font_size, labelpad=label_pad, loc=location)
        return self

    def setup_y_ticks(self, font_size=10, rotation=0):
        plt.yticks(fontsize=font_size, rotation=rotation)
        return self

    def setup_y_label(self, label, rotation=0, font_size=10, label_pad=0):
        plt.ylabel(label, rotation=rotation, fontsize=font_size, labelpad=label_pad)
        return self

    def plot(self, draw_x, draw_y, marker, color, name=""):
        line = plt.plot(draw_x, draw_y, marker=marker, color=color)
        self._legend[line[0]] = name
        return self

    def plot_line(self, line_: Line, marker, color, name=""):
        line = plt.plot(line_.x, line_.y, marker=marker, color=color)
        self._legend[line[0]] = name
        return self

    def scatter(self, draw_x, draw_y, marker, color, name=""):
        scatter = plt.scatter(draw_x, draw_y, marker=marker, rasterized=True, linewidths=0.01, color=color)
        self._legend[scatter] = name
        return self

    def show(self):
        plt.show(block=False)
        return self

    def show_last(self):
        plt.show(block=True)

    def legend(self):
        lines = []
        names = []
        for k in self._legend:
            lines.append(k)
            names.append(self._legend[k])
        self.ax.legend(lines, names)
        return self
