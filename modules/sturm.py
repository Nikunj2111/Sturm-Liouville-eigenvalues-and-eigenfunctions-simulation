from __future__ import annotations

import numpy as np

from modules.utils import validate_1d_array, validate_mode_count, validate_positive


def compute_eigenvalues(num_modes: int, length: float) -> np.ndarray:
    mode_count = validate_mode_count(num_modes)
    domain_length = validate_positive(length, "length")
    modes = np.arange(1, mode_count + 1, dtype=float)
    return (modes**2 * np.pi**2) / (domain_length**2)


def compute_eigenfunctions(num_modes: int, length: float, x: np.ndarray) -> dict[int, np.ndarray]:
    mode_count = validate_mode_count(num_modes)
    domain_length = validate_positive(length, "length")
    domain = validate_1d_array("x", x, minimum_size=2)

    return {
        mode: np.sin((mode * np.pi * domain) / domain_length)
        for mode in range(1, mode_count + 1)
    }


def compute_boundary_residuals(num_modes: int, length: float, x: np.ndarray) -> list[dict[str, float]]:
    eigenfunctions = compute_eigenfunctions(num_modes=num_modes, length=length, x=x)
    rows: list[dict[str, float]] = []

    for mode, values in eigenfunctions.items():
        left_residual = float(abs(values[0]))
        right_residual = float(abs(values[-1]))
        rows.append(
            {
                "mode": mode,
                "left_residual": left_residual,
                "right_residual": right_residual,
                "max_boundary_residual": max(left_residual, right_residual),
            }
        )

    return rows

