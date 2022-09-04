from algorithms.regime_map import regime_map
from runner import *
from runners import run_time_series, run_bifurcation

if __name__ == "__main__":
    print("Run")

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

    # todo: experiment
    # run_time_series.without_chaos_composition_parallel()

    # Показать график бифуркации
    # run_bifurcation.without_chaos()

    # Показать графики бифуркации с разными шумами
    # run_bifurcation.compare_chaos_bifurcation()

    # Показать график бифуркации с absorbing area
    # run_bifurcation.with_absorbing_area()

    # Показать показатель Ляпунова
    # run_lyapunov()

    # Показать лестницу Ламерея
    # run_lamerei()
    # run_lamerei_fast_zero()
    # run_lamerei_fast_zero_segment()

    # Показать график бифуркации и корни
    # run_bifurcation_with_equilibrium()

    # Показать графики равновесий
    # run_equilibrium()

    # Просчитать карту режимов
    # run_regime_map()

    # Матожидание
    # run_mean()

    # Усредненное матожидание
    # run_cyclic_mean()

    # Дисперсия
    # run_variance()

    # Циклическая дисперсия
    # run_cyclic_variance()

    # Функция стохастической чувствительности
    # run_stochastic_sensitivity_b_noise()
    # run_stochastic_sensitivity_a_noise()
    # run_stochastic_sensitivity_additive_noise()

    # run_stochastic_sensitivity_b_noise_1()
    # run_stochastic_sensitivity_b_noise_2()
    # run_stochastic_sensitivity_b_noise_3()
    # run_stochastic_sensitivity_b_noise_4()

    # График стохастической чувствительности
    # run_m_b_beta_noise()
    # run_m_b_alpha_noise()
    # run_m_b_additive_noise()

    # Выгрузить в файл данные по функции стохастической чувствительности
    # run_stochastic_sensitivity_b_noise_to_file()
    # run_stochastic_sensitivity_a_noise_to_file()
    # run_stochastic_sensitivity_additive_noise_to_file()

    # run_machalanobis_alpha_noise()
    # run_machalanobis_beta_noise()
    # run_machalanobis_additive_noise()

    # run_euclid_alpha_noise()
    # run_euclid_beta_noise()
    # run_euclid_additive_noise()

    # critical_intensity_beta_noise()
    # critical_intensity_alpha_noise()
    # critical_intensity_additive_noise()
