from __future__ import annotations

import numpy as np

from modules import bessel, sturm
from modules.utils import build_domain_grid, validate_resolution


def compute_sturm_boundary_errors(
    num_modes: int,
    length: float,
    resolution: int,
) -> list[dict[str, float]]:
    x = build_domain_grid(length=length, resolution=resolution)
    return sturm.compute_boundary_residuals(num_modes=num_modes, length=length, x=x)


def compute_sturm_resolution_errors(
    num_modes: int,
    length: float,
    coarse_resolution: int,
    fine_resolution: int,
) -> list[dict[str, float]]:
    coarse_points = validate_resolution(coarse_resolution, name="coarse_resolution")
    fine_points = validate_resolution(fine_resolution, name="fine_resolution")

    if fine_points <= coarse_points:
        raise ValueError("fine_resolution must be greater than coarse_resolution.")

    coarse_x = build_domain_grid(length=length, resolution=coarse_points)
    fine_x = build_domain_grid(length=length, resolution=fine_points)
    coarse_functions = sturm.compute_eigenfunctions(num_modes=num_modes, length=length, x=coarse_x)
    fine_functions = sturm.compute_eigenfunctions(num_modes=num_modes, length=length, x=fine_x)

    rows: list[dict[str, float]] = []

    for mode in range(1, int(num_modes) + 1):
        interpolated = np.interp(fine_x, coarse_x, coarse_functions[mode])
        differences = fine_functions[mode] - interpolated
        rows.append(
            {
                "mode": mode,
                "max_difference": float(np.max(np.abs(differences))),
                "rmse": float(np.sqrt(np.mean(differences**2))),
            }
        )

    return rows


def compute_bessel_zero_errors(order: int, num_modes: int) -> list[dict[str, float]]:
    return bessel.compute_zero_residuals(order=order, num_modes=num_modes)

