from __future__ import annotations

import numpy as np


PLOT_COLORS = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
]


def validate_positive(value: float, name: str) -> float:
    numeric_value = float(value)
    if numeric_value <= 0:
        raise ValueError(f"{name} must be positive.")
    return numeric_value


def validate_mode_count(num_modes: int) -> int:
    integer_value = int(num_modes)
    if integer_value <= 0:
        raise ValueError("num_modes must be at least 1.")
    return integer_value


def validate_resolution(resolution: int, name: str = "resolution") -> int:
    integer_value = int(resolution)
    if integer_value < 2:
        raise ValueError(f"{name} must be at least 2.")
    return integer_value


def validate_order(order: int) -> int:
    integer_value = int(order)
    if integer_value not in (0, 1):
        raise ValueError("Only Bessel orders 0 and 1 are supported.")
    return integer_value


def validate_1d_array(name: str, values, minimum_size: int = 1) -> np.ndarray:
    array = np.asarray(values, dtype=float)
    if array.ndim != 1:
        raise ValueError(f"{name} must be a one-dimensional array.")
    if array.size < minimum_size:
        raise ValueError(f"{name} must contain at least {minimum_size} values.")
    return array


def build_domain_grid(length: float, resolution: int) -> np.ndarray:
    domain_length = validate_positive(length, "length")
    grid_resolution = validate_resolution(resolution)
    return np.linspace(0.0, domain_length, grid_resolution)


def build_radius_grid(radius_scale: float, resolution: int) -> np.ndarray:
    radius = validate_positive(radius_scale, "radius_scale")
    grid_resolution = validate_resolution(resolution)
    return np.linspace(0.0, radius, grid_resolution)

