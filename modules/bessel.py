from __future__ import annotations

import numpy as np
from scipy import special

from modules.utils import (
    validate_1d_array,
    validate_mode_count,
    validate_order,
    validate_positive,
)


def compute_bessel(order: int, x: np.ndarray) -> np.ndarray:
    bessel_order = validate_order(order)
    values = validate_1d_array("x", x)

    if bessel_order == 0:
        return special.j0(values)

    return special.j1(values)


def compute_zeros(order: int, num_modes: int) -> np.ndarray:
    bessel_order = validate_order(order)
    mode_count = validate_mode_count(num_modes)
    return special.jn_zeros(bessel_order, mode_count)


def compute_zero_residuals(order: int, num_modes: int) -> list[dict[str, float]]:
    bessel_order = validate_order(order)
    zeros = compute_zeros(order=bessel_order, num_modes=num_modes)
    values = compute_bessel(order=bessel_order, x=zeros)

    return [
        {
            "mode": index,
            "zero": float(zero),
            "abs_residual": float(abs(value)),
        }
        for index, (zero, value) in enumerate(zip(zeros, values), start=1)
    ]


def compute_radial_modes(
    order: int,
    radii: np.ndarray,
    num_modes: int,
    radius_scale: float = 1.0,
) -> dict[int, np.ndarray]:
    bessel_order = validate_order(order)
    radial_grid = validate_1d_array("radii", radii, minimum_size=2)
    scale = validate_positive(radius_scale, "radius_scale")
    zeros = compute_zeros(order=bessel_order, num_modes=num_modes)

    return {
        index: compute_bessel(order=bessel_order, x=(zero * radial_grid) / scale)
        for index, zero in enumerate(zeros, start=1)
    }

