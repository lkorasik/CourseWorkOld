import builder
import extrema
import lyapunov
from builder import Builder
from functions import Functions
from parameters import Parameters

if __name__ == "__main__":
    params = Parameters()

    r = extrema.get_cs(0, 1, 0.01, params.a, params.b)

    print("c_{-1}: ", r[0])
    print("c: ", r[1])
    print("c_1: ", r[2])

    Builder.bifurcation_with_c(
        params.get_time_range(),
        params.x_start,
        params.get_b_range(),
        params.a,
        0,
        1,
        params.precision * 100,
        False
    )

    exit(0)

    lyapunov.Lyapunov.calc(
        10e-0,
        1,
        params.get_b_range(),
        params.x_start,
        params.get_time_range(),
        params.time,
        True
    )

    Builder.bifurcation(
        params.get_time_range(),
        params.x_start,
        params.get_b_range(),
        params.a,
        True
    )
    Builder.bifurcation_stables(
        params.get_time_range(),
        params.x_start,
        params.get_b_range(),
        params.a,
        params.x_start,
        params.precision,
        Functions.h,
        Functions.dh,
        True,
        params.x1_color,
        params.x2_color,
        params.x_1_color,
        params.biff_color
    )

    Builder.stable(
        params.a,
        params.x_start,
        params.get_b_range(),
        params.precision,
        Functions.h,
        Functions.dh,
        Functions.df,
        False,
        params.x1_color,
        params.x2_color,
        params.x_1_color
    )

    '''
    lyapunov.Lyapunov.calc(
        10e-0,
        1,
        params.get_b_range(),
        params.x_start,
        params.get_time_range(),
        params.time,
        True
    )
    Builder.bifurcation(
        params.get_time_range(),
        params.x_start,
        params.get_b_range(),
        params.a,
        True
    )
    Builder.bifurcation_stables(
        params.get_time_range(),
        params.x_start,
        params.get_b_range(),
        params.a,
        params.x_start,
        params.precision,
        Functions.h,
        Functions.dh,
        True,
        params.x1_color,
        params.x2_color,
        params.x_1_color,
        params.biff_color
    )
    Builder.time_series(
        params.get_time_range(),
        params.x_start,
        params.b,
        params.a,
        params.skip,
        True
    )
    Builder.lamerei(
        params.a,
        params.x_start,
        params.b,
        params.get_time_range(),
        params.skip,
        False
    )
    Builder.stable(
        params.a,
        params.x_start,
        params.get_b_range(),
        params.precision,
        Functions.h,
        Functions.dh,
        Functions.df,
        False,
        params.x1_color,
        params.x2_color,
        params.x_1_color
    )
    '''
