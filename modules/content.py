APP_TITLE = "Interactive Visualizer for Eigenvalues, Eigenfunctions, Sturm-Liouville Problems, and Bessel Functions"

HOME_DESCRIPTION = (
    "This Streamlit app computes closed-form eigenvalues and eigenfunctions for a basic "
    "Sturm-Liouville problem, visualizes Bessel functions of the first kind, and connects "
    "the mathematics to signal processing and acoustics."
)

TOPICS = [
    "Eigenvalues and Eigenfunctions",
    "Sturm-Liouville Problems",
    "Bessel Functions",
    "Applications in Telecommunications, Signal Processing, Acoustics, and Vibrations",
]

CORE_CONCEPTS = {
    "Eigenvalues": "Eigenvalues are special parameter values that allow a boundary value problem to admit non-trivial solutions.",
    "Eigenfunctions": "Eigenfunctions are the corresponding non-zero solution shapes associated with each eigenvalue.",
    "Sturm-Liouville Problems": "A Sturm-Liouville problem combines a differential equation with boundary conditions to produce an orthogonal family of modes.",
    "Bessel Functions": "Bessel functions arise naturally in cylindrical and circular geometries such as membranes, waveguides, and radial vibration models.",
}

STURM_TEXT = (
    "For the model problem y'' + lambda y = 0 with y(0) = 0 and y(L) = 0, the allowed "
    "eigenvalues are lambda_n = n^2 pi^2 / L^2 and the eigenfunctions are y_n(x) = sin(n pi x / L)."
)

EIGEN_TEXT = (
    "Comparing several modes at once shows how higher modes oscillate more rapidly and how "
    "the eigenvalues grow quadratically with the mode index."
)

BESSEL_TEXT = (
    "The Bessel equation x^2 y'' + x y' + (x^2 - n^2)y = 0 appears in circular and cylindrical "
    "systems. This app focuses on J0(x) and J1(x), together with their positive zeros."
)

APPLICATION_TEXT = {
    "telecom": (
        "Orthogonal functions underpin Fourier-style signal decomposition, filtering, and compact "
        "representation of periodic signals used in telecommunications and signal processing."
    ),
    "acoustics": (
        "Bessel functions model radial behavior in circular membranes, so their zeros and mode "
        "shapes help describe drum vibrations, resonance, and cylindrical wave patterns."
    ),
}

ERROR_ANALYSIS_TEXT = (
    "The error analysis section checks how well the computed results satisfy boundary conditions, "
    "how coarse sampling affects reconstructed eigenfunction curves, and how close each numerically "
    "computed Bessel zero is to a true root."
)

SUMMARY_TEXT = (
    "The project combines exact formulas, numerical special functions, and visual interpretation. "
    "It is designed to produce clean graphs and tables that can be used directly in an assignment report."
)

