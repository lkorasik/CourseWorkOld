from functools import partial, reduce

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import numpy.random

import functions
from lyapunov import lyapunov
from new.builder.bifurcation import bifurcation
from new.builder.bifurcation_with_equilibrium import bifurcation_with_equilibrium
from new.builder.bifurcation_with_absorbing_area import bifurcation_with_absorbing_area
from new.builder.bifurcation_with_ssf import bifurcation_with_ssf
from new.builder.converter import convert_dict_to_lists
from new.builder.cyclical_mean import cyclical_mean
from new.builder.cyclical_variance import cyclical_variance
from new.builder.find_all_roots import find_all_roots
from new.builder.lamerei import lamerei
from new.builder.m_b import m_b
from new.builder.mean import mean
from new.builder.equilibrium import equilibrium
from new.builder.time_series import time_series
from new.builder.variance import variance
from plotter import Plotter
from regime_map import regime_map
from runner import run_time_series, run_bifurcation, run_bifurcation_with_absorbing_area, run_lyapunov, run_lamerei, \
    run_bifurcation_with_equilibrium, run_equilibrium, run_time_series_2, run_time_series_3, run_bifurcation_2, \
    run_mean, run_cyclic_mean, run_variance, run_cyclic_variance, run_stochastoc_sensetivity, run_m_b

if __name__ == "__main__":

    # Показать график временного ряда
    # run_time_series()
    # run_time_series_2()

    # Показать график бифуркации
    # run_bifurcation()

    # Показать график бифуркации с
    # run_bifurcation_with_absorbing_area()

    # Показать показатель Ляпунова
    # run_lyapunov()

    # Показать лестницу Ламерея
    # run_lamerei()

    # Показать график бифуркации и корни
    # run_bifurcation_with_equilibrium()

    # Показать графики равновесий
    # run_equilibrium()

    # regime_map(
    #     x_start=0.2,
    #     a_range=np.arange(0.01, 2, 0.01),
    #     b_range=np.arange(0.01, 0.6, 0.01),
    #     time_range=range(1, 10000 + 1),
    #     f=functions.f)

    # find_all_roots(
    #     x_range=np.arange(0, 1.5, 0.01),
    #     a_range=np.arange(0.01, 2, 0.01),
    #     b_range=np.arange(0.01, 0.6, 0.01),
    #     precision=0.001
    # )

    # Показать графики временных рядов с разными шумами
    # run_time_series_3()

    # Показать графики бифуркации с разными шумами
    # run_bifurcation_2()

    # Матожидание
    # run_mean()

    # Усредненное матожидание
    # run_cyclic_mean()

    # Дисперсия
    # run_variance()

    # Циклическая дисперсия
    # run_cyclic_variance()

    # Функция стохастической чувствительности
    # run_stochastoc_sensetivity()

    # График стохастической чувствительности
    run_m_b()
