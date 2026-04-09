from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure

from modules.utils import PLOT_COLORS


def _styled_figure(figsize: tuple[float, float] = (8.5, 4.8)) -> tuple[Figure, plt.Axes]:
    figure, axis = plt.subplots(figsize=figsize, layout="constrained")
    axis.grid(alpha=0.25, linestyle="--", linewidth=0.6)
    return figure, axis


def plot_eigenfunctions(x: np.ndarray, eigenfunctions: dict[int, np.ndarray], length: float) -> Figure:
    figure, axis = _styled_figure()
    for mode, values in eigenfunctions.items():
        axis.plot(x, values, label=fr"$y_{mode}(x)$", color=PLOT_COLORS[(mode - 1) % len(PLOT_COLORS)])

    axis.axhline(0.0, color="#444444", linewidth=0.8)
    axis.set_title(f"Eigenfunctions on [0, {length:.2f}]")
    axis.set_xlabel("x")
    axis.set_ylabel("y_n(x)")
    axis.legend(loc="upper right")
    return figure


def plot_eigenvalue_trend(eigenvalues: np.ndarray, length: float) -> Figure:
    figure, axis = _styled_figure()
    modes = np.arange(1, len(eigenvalues) + 1)
    axis.plot(modes, eigenvalues, marker="o", color=PLOT_COLORS[0])
    axis.set_title(f"Eigenvalue Growth for L = {length:.2f}")
    axis.set_xlabel("Mode n")
    axis.set_ylabel(r"$\lambda_n$")
    return figure


def plot_bessel(x: np.ndarray, y: np.ndarray, order: int) -> Figure:
    figure, axis = _styled_figure()
    axis.plot(x, y, color=PLOT_COLORS[1], label=fr"$J_{order}(x)$")
    axis.axhline(0.0, color="#444444", linewidth=0.8)
    axis.set_title(f"Bessel Function of the First Kind, Order {order}")
    axis.set_xlabel("x")
    axis.set_ylabel(fr"$J_{order}(x)$")
    axis.legend(loc="upper right")
    return figure


def plot_radial_modes(radii: np.ndarray, modes: dict[int, np.ndarray], order: int) -> Figure:
    figure, axis = _styled_figure()
    for mode, values in modes.items():
        axis.plot(radii, values, label=fr"$R_{mode}(r)$", color=PLOT_COLORS[(mode - 1) % len(PLOT_COLORS)])

    axis.axhline(0.0, color="#444444", linewidth=0.8)
    axis.set_title(f"Radial Vibration Modes from $J_{order}$")
    axis.set_xlabel("r")
    axis.set_ylabel("Amplitude")
    axis.legend(loc="upper right")
    return figure


def plot_error_metric(
    rows: list[dict[str, float]],
    x_key: str,
    y_key: str,
    title: str,
    y_label: str,
) -> Figure:
    figure, axis = _styled_figure()
    x_values = [row[x_key] for row in rows]
    y_values = [row[y_key] for row in rows]
    axis.plot(x_values, y_values, marker="o", color=PLOT_COLORS[3])
    axis.set_title(title)
    axis.set_xlabel(x_key.replace("_", " ").title())
    axis.set_ylabel(y_label)
    return figure


def plot_signal_decomposition(
    x: np.ndarray,
    original_signal: np.ndarray | None = None,
    components: dict[str, np.ndarray] | None = None,
    reconstructed_signal: np.ndarray | None = None,
) -> Figure:
    time = np.asarray(x, dtype=float)

    if components is None:
        components = {
            "Fundamental": np.sin(2 * np.pi * time),
            "Third Harmonic": 0.5 * np.sin(6 * np.pi * time),
        }

    if original_signal is None:
        original_signal = np.sum(list(components.values()), axis=0)

    if reconstructed_signal is None:
        reconstructed_signal = np.sum(list(components.values()), axis=0)

    figure, axes = plt.subplots(2, 1, figsize=(8.5, 6.2), sharex=True, layout="constrained")

    axes[0].plot(time, original_signal, color=PLOT_COLORS[0], label="Original Signal")
    axes[0].plot(time, reconstructed_signal, color=PLOT_COLORS[3], linestyle="--", label="Reconstructed Signal")
    axes[0].set_title("Signal Decomposition and Reconstruction")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(alpha=0.25, linestyle="--", linewidth=0.6)
    axes[0].legend(loc="upper right")

    for index, (label, values) in enumerate(components.items()):
        axes[1].plot(time, values, label=label, color=PLOT_COLORS[index % len(PLOT_COLORS)])

    axes[1].set_xlabel("Normalized Time")
    axes[1].set_ylabel("Component Value")
    axes[1].grid(alpha=0.25, linestyle="--", linewidth=0.6)
    axes[1].legend(loc="upper right")
    return figure

