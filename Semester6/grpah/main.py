from math import sqrt, cos, sin

import numpy
import numpy as np

from core.algorithms.new import regime_map, ellips
from core.algorithms.new.attractor import basin_of_attractor
from core.algorithms.old.bifurcation import bifurcation
from core.algorithms.time_series import time_series
from core.utils.convert_dict_to_lists import convert_dict_to_lists
from core.utils.is_out_of_bounds import is_out_of_bounds
from core.utils.convert_dict_to_lists import convert_dict_to_lists
from core.utils.new_is_out_of_bounds import new_is_out_of_bounds
from models.new_new_model import function
from runners.new import run_phase_portrait, new_bif, run_regime_map
from runners.new.run_phase_portrait import run1
from runners.new_new import new_new_run_phase_portrait, new_new_run_bifurcation, new_new_regime_map, attr, new_new_bif
from runners.old import run_bifurcation, run_time_series, run_others
from visual.line import Line
from visual.plotter import Plotter
from visual.values import scale, grid, markers, colors

from collections import Counter

if __name__ == "__main__":
    print("Run")

    # ----- Временные ряды -----
    # Показать график временного ряда
    # run_time_series.without_chaos()
    # run_time_series.different_noises()

    # run_time_series.no_noise()
    # run_time_series.beta_noise()
    # run_time_series.alpha_noise()
    # run_time_series.additive_noise()

    # run_time_series.compare_noise()
    # run_time_series.without_chaos_composition()

    # run_time_series.beta_noise_can_drop()

    # run_time_series.cycle_2()
    # run_time_series.chaos()
    # ----- Временные ряды -----

    # ----- Бифуркация -----
    # Показать график бифуркации
    # run_bifurcation.without_chaos()

    # Показать графики бифуркации с разными шумами
    # run_bifurcation.compare_chaos_bifurcation()

    # Показать график бифуркации с absorbing area
    # run_bifurcation.with_absorbing_area()

    # Показать график бифуркации и корни
    # run_bifurcation.with_equilibrium()
    # ----- Бифуркация -----

    # ----- Показатель Ляпунова -----
    # run_others.run_lyapunov()
    # ----- Показатель Ляпунова -----

    # ----- Лестницу Ламерея -----
    # run_lamerei.default()
    # run_lamerei.fast_zero()
    # run_lamerei.fast_zero_segment()
    # ----- Лестницу Ламерея -----

    # ----- Графики равновесий -----
    # run_others.run_equilibrium()
    # ----- Графики равновесий -----

    # ----- Просчитать карту режимов -----
    # run_others.run_regime_map()
    # ----- Просчитать карту режимов -----

    # ----- Матожидание -----
    # run_mean.single()
    # run_mean.cyclic()
    # ----- Матожидание -----

    # ----- Дисперсия -----
    # run_variance.single()
    # run_variance.cyclic()
    # ----- Дисперсия -----

    # ----- Функция стохастической чувствительности -----
    # run_stochastic_sensitivity.a_noise()
    # run_stochastic_sensitivity.b_noise()
    # run_stochastic_sensitivity.additive_noise()
    #
    # run_stochastic_sensitivity.b_noise_1()
    # run_stochastic_sensitivity.b_noise_2()
    # run_stochastic_sensitivity.b_noise_3()
    # run_stochastic_sensitivity.b_noise_4()

    # Выгрузить в файл данные по функции стохастической чувствительности
    # run_stochastic_sensitivity.b_noise_to_file()
    # run_stochastic_sensitivity.a_noise_to_file()
    # run_stochastic_sensitivity.additive_noise_to_file()
    # ----- Функция стохастической чувствительности -----

    # ----- График стохастической чувствительности -----
    # run_m_b.beta_noise()
    # run_m_b.alpha_noise()
    # run_m_b.additive_noise()
    # ----- График стохастической чувствительности -----

    # ----- Метрики -----
    # run_metrics.machalanobis_alpha_noise()
    # run_metrics.machalanobis_beta_noise()
    # run_metrics.machalanobis_additive_noise()
    #
    # run_metrics.euclid_alpha_noise()
    # run_metrics.euclid_beta_noise()
    # run_metrics.euclid_additive_noise()
    # ----- Метрики -----

    # ----- Критическая интенсивность -----
    # run_critical_intensity.beta_noise()
    # run_critical_intensity.alpha_noise()
    # run_critical_intensity.additive_noise()
    # ----- Критическая интенсивность -----

    #                                                        ____________
    #                                  (`-..________....---''  ____..._.-`
    #                                   \\`._______.._,.---'''     ,'
    #                                   ; )`.      __..-'`-.      /
    #                                  / /     _.-' _,.;;._ `-._,'
    #                                 / /   ,-' _.-'  //   ``--._``._
    #                               ,','_.-' ,-' _.- (( =-    -. `-._`-._____
    #                             ,;.''__..-'   _..--.\\.--'````--.._``-.`-._`.
    #              _          |\,' .-''        ```-'`---'`-...__,._  ``-.`-.`-.`.
    #   _     _.-,'(__)\__)\-'' `     ___  .          `     \      `--._
    # ,',)---' /|)          `     `      ``-.   `     /     /     `     `-.
    # \_____--.  '`  `               __..-.  \     . (   < _...-----..._   `.
    #  \_,--..__. \\ .-`.\----'';``,..-.__ \  \      ,`_. `.,-'`--'`---''`.  )
    #            `.\`.\  `_.-..' ,'   _,-..'  /..,-''(, ,' ; ( _______`___..'__
    #                    ((,(,__(    ((,(,__,'  ``'-- `'`.(\  `.,..______   SSt
    #                                                       ``--------..._``--.__
    #

    # ===== 7 СЕМЕСТР =====

    # ----- Фазовые портреты -----
    # run_phase_portrait.run0()
    # run_phase_portrait.run1()
    # run_phase_portrait.run2()
    # run_phase_portrait.run3()
    # run_phase_portrait.run4()
    # run_phase_portrait.run5()
    # run_phase_portrait.run6()
    # run_phase_portrait.run7()
    # ----- Фазовые портреты -----

    # ----- График бифуркации -----
    # new_bif.run1()
    # new_bif.run2()
    # new_bif.run3()
    # new_bif.run_la()
    # new_bif.run4()
    # new_bif.run_combine()
    # new_bif.run_bif_with_equilibrium()
    # ----- График бифуркации -----

    # ----- Карта режимов -----
    # run_regime_map.run_preview()
    # run_regime_map.run_full()
    # run_regime_map.run    _new_preview()  
    # run_regime_map.run_new_full()
    # run_regime_map.run0()
    # ----- Карта режимов -----

    # ----- Временные ряды -----
    # runners.new.run_time_series.run_2_cycle_0()
    # runners.new.run_time_series.run_2_cycle_1()
    # runners.new.run_time_series.run_2_cycle_2()
    # runners.new.run_time_series.run_2_cycle_3()
    # runners.new.run_time_series.run_2_cycle_4()
    # ----- Временные ряды -----

    # a = 1
    # b = 0.4
    # γ = 0.14
    # area_of_attractor(
    #     file_path="C:\\Users\\lkora\\Desktop\\ktData5\\",
    #     x_range=np.arange(0, 2.5, 1),
    #     y_range=np.arange(0, 2.5, 1),
    #     time_range=range(10000),
    #     cycle=2,
    #     g=lambda x, y: function.__y(a, b, γ, x, y),
    #     f=lambda x, y: function.__x(a, b, γ, x, y),
    #     gc=lambda γ, x, y: function.__y(a, b, γ, x, y),
    #     fc=lambda γ, x, y: function.__x(a, b, γ, x, y),
    #     x_start=0.2,
    # y_start = 0.2
    # )

    #                                                        ____________
    #                                  (`-..________....---''  ____..._.-`
    #                                   \\`._______.._,.---'''     ,'
    #                                   ; )`.      __..-'`-.      /
    #                                  / /     _.-' _,.;;._ `-._,'
    #                                 / /   ,-' _.-'  //   ``--._``._
    #                               ,','_.-' ,-' _.- (( =-    -. `-._`-._____
    #                             ,;.''__..-'   _..--.\\.--'````--.._``-.`-._`.
    #              _          |\,' .-''        ```-'`---'`-...__,._  ``-.`-.`-.`.
    #   _     _.-,'(__)\__)\-'' `     ___  .          `     \      `--._
    # ,',)---' /|)          `     `      ``-.   `     /     /     `     `-.
    # \_____--.  '`  `               __..-.  \     . (   < _...-----..._   `.
    #  \_,--..__. \\ .-`.\----'';``,..-.__ \  \      ,`_. `.,-'`--'`---''`.  )
    #            `.\`.\  `_.-..' ,'   _,-..'  /..,-''(, ,' ; ( _______`___..'__
    #                    ((,(,__(    ((,(,__,'  ``'-- `'`.(\  `.,..______   SSt
    #                                                       ``--------..._``--.__
    #

    # ----- Фазовые портреты -----
    # new_new_run_phase_portrait.run0()
    # new_new_run_phase_portrait.run1()
    # new_new_run_phase_portrait.run2()
    # new_new_run_phase_portrait.run3()
    # new_new_run_phase_portrait.run4()
    # new_new_run_phase_portrait.run6()
    # new_new_run_phase_portrait.run7()
    # new_new_run_phase_portrait.run8()
    # new_new_run_phase_portrait.run9()
    new_new_run_phase_portrait.run10()
    # ----- Фазовые портреты -----

    # ----- Бифуркационная диаграмма -----
    # new_new_run_bifurcation.run1()
    # new_new_run_bifurcation.run2()
    # new_new_run_bifurcation.run3()
    # new_new_run_bifurcation.run4()
    # ----- Бифуркационная диаграмма -----

    # ----- Карта режимов -----
    # new_new_regime_map.run0()
    # new_new_regime_map.run1()
    # ----- Карта режимов -----

    # a = 1
    # # b = 0.4
    # b = 0.445
    # # b = 0.4
    # # σ = 0.03
    # σ = 0.27
    # # σ = 0.2
    # # σ = 0.1
    # basin_of_attractor(
    #     file_path="C:\\Users\\lkora\\Desktop\\kt6\\",
    #     # file_path="C:\\Users\\lkora\\Desktop\\ktData7\\",
    #     x_range=np.arange(0, 1.0, 0.1),
    #     y_range=np.arange(0, 1.0, 0.1),
    #     time_range=range(10000),
    #     g=lambda x, y: function.__y(a, b, σ, x, y),
    #     f=lambda x, y: function.__x(a, b, σ, x, y),
    #     R=4
    # )

    # new_new_regime_map.run5()
    # new_new_bif.run0()
    # new_new_bif.run1()
    # new_new_bif.run2()
    # new_new_bif.run3()
    # new_new_bif.run4()
    # attr.run1()

    # ellips.run0()
