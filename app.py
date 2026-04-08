from __future__ import annotations

import numpy as np
import streamlit as st
from matplotlib import pyplot as plt

from modules import bessel, content, error_analysis, plots, sturm, utils


def show_figure(figure) -> None:
    st.pyplot(figure, clear_figure=True, use_container_width=True)
    plt.close(figure)


def render_home_page() -> None:
    st.title(content.APP_TITLE)
    st.write(content.HOME_DESCRIPTION)
    st.subheader("Topics Covered")
    st.write(content.TOPICS)

    st.subheader("Core Concepts")
    for heading, explanation in content.CORE_CONCEPTS.items():
        st.markdown(f"**{heading}**")
        st.write(explanation)

    st.subheader("Core Formula Sheet")
    st.latex(r"\lambda_n = \frac{n^2 \pi^2}{L^2},\quad y_n(x)=\sin\left(\frac{n\pi x}{L}\right)")
    st.latex(r"x^2y'' + xy' + (x^2 - n^2)y = 0,\quad R_n(r) = J_n\left(\alpha_n r / a\right)")
    st.latex(r"f(t) = \sum_{k=1}^{N} a_k \sin(k \omega t) + b_k \cos(k \omega t)")


def render_sturm_page() -> None:
    st.title("Sturm-Liouville")
    st.write(content.STURM_TEXT)
    st.latex(r"y'' + \lambda y = 0,\quad y(0)=0,\quad y(L)=0")
    st.latex(r"\lambda_n = \frac{n^2 \pi^2}{L^2},\quad y_n(x)=\sin\left(\frac{n\pi x}{L}\right)")

    st.sidebar.subheader("Sturm-Liouville Parameters")
    num_modes = st.sidebar.slider("Number of modes", min_value=1, max_value=8, value=4, key="sturm_modes")
    length = st.sidebar.number_input("Domain length L", min_value=0.5, max_value=10.0, value=1.0, step=0.5, key="sturm_length")
    resolution = st.sidebar.slider("Resolution", min_value=100, max_value=1000, value=400, step=50, key="sturm_resolution")

    x = utils.build_domain_grid(length=length, resolution=resolution)
    eigenvalues = sturm.compute_eigenvalues(num_modes=num_modes, length=length)
    eigenfunctions = sturm.compute_eigenfunctions(num_modes=num_modes, length=length, x=x)
    eigenvalue_rows = [
        {"mode": mode, "eigenvalue": float(value)}
        for mode, value in enumerate(eigenvalues, start=1)
    ]

    table_column, plot_column = st.columns((1, 2))
    with table_column:
        st.subheader("Eigenvalue Table")
        st.table(eigenvalue_rows)
    with plot_column:
        st.subheader("Eigenfunction Plot")
        show_figure(plots.plot_eigenfunctions(x=x, eigenfunctions=eigenfunctions, length=length))

    st.subheader("Eigenvalue Trend")
    show_figure(plots.plot_eigenvalue_trend(eigenvalues=eigenvalues, length=length))


def render_eigen_page() -> None:
    st.title("Eigenvalues & Eigenfunctions")
    st.write(content.EIGEN_TEXT)
    st.latex(r"\lambda_n = \frac{n^2 \pi^2}{L^2}")
    st.latex(r"y_n(x)=\sin\left(\frac{n\pi x}{L}\right)")
    st.latex(r"\int_0^L y_m(x)y_n(x)\,dx = 0 \quad \text{for } m \neq n")

    st.sidebar.subheader("Eigenvalue View Parameters")
    num_modes = st.sidebar.slider("Modes to compare", min_value=1, max_value=8, value=5, key="eigen_modes")
    length = st.sidebar.number_input("Domain length for comparison", min_value=0.5, max_value=10.0, value=1.0, step=0.5, key="eigen_length")
    resolution = st.sidebar.slider("Curve resolution", min_value=100, max_value=1000, value=500, step=50, key="eigen_resolution")

    x = utils.build_domain_grid(length=length, resolution=resolution)
    eigenvalues = sturm.compute_eigenvalues(num_modes=num_modes, length=length)
    eigenfunctions = sturm.compute_eigenfunctions(num_modes=num_modes, length=length, x=x)
    rows = [
        {"n": mode, "Eigenvalue": float(value)}
        for mode, value in enumerate(eigenvalues, start=1)
    ]

    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Mode Table")
        st.table(rows)
    with right_column:
        st.subheader("Mode Curves")
        show_figure(plots.plot_eigenfunctions(x=x, eigenfunctions=eigenfunctions, length=length))

    st.subheader("Quadratic Growth of Eigenvalues")
    show_figure(plots.plot_eigenvalue_trend(eigenvalues=eigenvalues, length=length))


def render_bessel_page() -> None:
    st.title("Bessel Functions")
    st.write(content.BESSEL_TEXT)
    st.latex(r"x^2y'' + xy' + (x^2 - n^2)y = 0")
    st.latex(r"R_n(r) = J_n\left(\alpha_n r / a\right)")
    st.latex(r"J_n(\alpha_k) = 0")

    st.sidebar.subheader("Bessel Parameters")
    order = st.sidebar.selectbox("Bessel order", options=[0, 1], index=0, key="bessel_order")
    x_max = st.sidebar.slider("x range max", min_value=5.0, max_value=30.0, value=20.0, step=1.0, key="bessel_xmax")
    num_modes = st.sidebar.slider("Number of zeros / modes", min_value=1, max_value=6, value=4, key="bessel_modes")
    resolution = st.sidebar.slider("Curve resolution", min_value=200, max_value=1200, value=600, step=50, key="bessel_resolution")

    x = np.linspace(0.0, x_max, resolution)
    radii = utils.build_radius_grid(radius_scale=1.0, resolution=resolution)
    values = bessel.compute_bessel(order=order, x=x)
    zeros = bessel.compute_zeros(order=order, num_modes=num_modes)
    zero_rows = [{"mode": mode, "zero": float(zero)} for mode, zero in enumerate(zeros, start=1)]
    radial_modes = bessel.compute_radial_modes(order=order, radii=radii, num_modes=num_modes)

    table_column, plot_column = st.columns((1, 2))
    with table_column:
        st.subheader("Zeros Table")
        st.table(zero_rows)
    with plot_column:
        st.subheader(f"$J_{order}(x)$ Curve")
        show_figure(plots.plot_bessel(x=x, y=values, order=order))

    st.subheader("Radial Vibration Modes")
    show_figure(plots.plot_radial_modes(radii=radii, modes=radial_modes, order=order))


def render_applications_page() -> None:
    st.title("Applications")

    st.subheader("Telecommunications and Signal Processing")
    st.write(content.APPLICATION_TEXT["telecom"])
    st.latex(r"f(t) = \sum_{k=1}^{N} a_k \sin(k \omega t) + b_k \cos(k \omega t)")
    st.latex(r"a_k = \frac{2}{T}\int_0^T f(t)\sin(k\omega t)\,dt,\quad b_k = \frac{2}{T}\int_0^T f(t)\cos(k\omega t)\,dt")
    telecom_x = np.linspace(0.0, 1.0, 600)
    show_figure(plots.plot_signal_decomposition(x=telecom_x))

    st.subheader("Acoustics and Vibrations")
    st.write(content.APPLICATION_TEXT["acoustics"])
    st.latex(r"R_n(r) = J_n\left(\alpha_n r / a\right),\quad J_n(\alpha_n)=0")
    radii = utils.build_radius_grid(radius_scale=1.0, resolution=400)
    radial_modes = bessel.compute_radial_modes(order=0, radii=radii, num_modes=3)
    show_figure(plots.plot_radial_modes(radii=radii, modes=radial_modes, order=0))


def render_error_analysis_page() -> None:
    st.title("Error Analysis")
    st.write(content.ERROR_ANALYSIS_TEXT)
    st.latex(r"R_{\mathrm{bc},n} = \max\left(|y_n(0)|, |y_n(L)|\right)")
    st.latex(r"\mathrm{RMSE}_n = \sqrt{\frac{1}{M}\sum_{i=1}^{M}\left(y_n^{\mathrm{fine}}(x_i)-y_n^{\mathrm{interp}}(x_i)\right)^2}")
    st.latex(r"\left|J_n(\alpha_k)\right| \approx 0")

    st.sidebar.subheader("Error Analysis Parameters")
    num_modes = st.sidebar.slider("Modes for error analysis", min_value=1, max_value=6, value=4, key="error_modes")
    length = st.sidebar.number_input("Domain length for error analysis", min_value=0.5, max_value=10.0, value=1.0, step=0.5, key="error_length")
    coarse_resolution = st.sidebar.slider("Coarse resolution", min_value=21, max_value=201, value=51, step=10, key="error_coarse")
    fine_resolution = st.sidebar.slider("Fine resolution", min_value=101, max_value=1001, value=401, step=50, key="error_fine")
    order = st.sidebar.selectbox("Bessel order for zero check", options=[0, 1], index=0, key="error_order")

    boundary_rows = error_analysis.compute_sturm_boundary_errors(
        num_modes=num_modes,
        length=length,
        resolution=fine_resolution,
    )
    resolution_rows = error_analysis.compute_sturm_resolution_errors(
        num_modes=num_modes,
        length=length,
        coarse_resolution=coarse_resolution,
        fine_resolution=fine_resolution,
    )
    bessel_rows = error_analysis.compute_bessel_zero_errors(order=order, num_modes=num_modes)

    st.subheader("Boundary Condition Residuals")
    st.table(boundary_rows)
    show_figure(
        plots.plot_error_metric(
            rows=boundary_rows,
            x_key="mode",
            y_key="max_boundary_residual",
            title="Sturm-Liouville Boundary Residual by Mode",
            y_label="Max Boundary Residual",
        )
    )

    st.subheader("Resolution Sensitivity")
    st.table(resolution_rows)
    show_figure(
        plots.plot_error_metric(
            rows=resolution_rows,
            x_key="mode",
            y_key="max_difference",
            title="Coarse-vs-Fine Curve Difference",
            y_label="Max Difference",
        )
    )

    st.subheader("Bessel Zero Verification")
    st.table(bessel_rows)
    show_figure(
        plots.plot_error_metric(
            rows=bessel_rows,
            x_key="mode",
            y_key="abs_residual",
            title="Absolute Residual at Each Bessel Zero",
            y_label="|J_n(alpha_k)|",
        )
    )


def main() -> None:
    st.set_page_config(page_title="Math III Visualizer", layout="wide")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        [
            "Home",
            "Sturm-Liouville",
            "Eigenvalues & Eigenfunctions",
            "Bessel Functions",
            "Applications",
            "Error Analysis",
        ],
    )
    st.sidebar.caption("Built with Streamlit, NumPy, SciPy, and Matplotlib.")

    if page == "Home":
        render_home_page()
    elif page == "Sturm-Liouville":
        render_sturm_page()
    elif page == "Eigenvalues & Eigenfunctions":
        render_eigen_page()
    elif page == "Bessel Functions":
        render_bessel_page()
    elif page == "Applications":
        render_applications_page()
    else:
        render_error_analysis_page()


if __name__ == "__main__":
    main()
