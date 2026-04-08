## Project Overview

This project is a simple Streamlit application for a Math III assignment. It explains and visualizes:

- eigenvalues
- eigenfunctions
- a basic Sturm-Liouville boundary value problem
- Bessel functions of the first kind
- simple applications in signal processing and acoustics
- basic error analysis for the computed results

The app uses exact formulas for the Sturm-Liouville section and SciPy's Bessel utilities for the Bessel section. All graphs are drawn with Matplotlib.

## What The Project Does

The application has 6 pages in the Streamlit sidebar.

### 1. Home

This page shows the project title, topic list, short theory notes, and the main formulas used in the app.

### 2. Sturm-Liouville

This page works with the boundary value problem:

`y'' + lambda y = 0`

with boundary conditions:

`y(0) = 0` and `y(L) = 0`

It displays:

- the governing formulas
- the eigenvalue formula
- the eigenfunction formula
- a table of eigenvalues
- plots of eigenfunctions
- a graph of eigenvalue growth

### 3. Eigenvalues and Eigenfunctions

This page compares several modes together. It includes:

- the eigenvalue formula
- the eigenfunction formula
- the orthogonality relation
- a mode-wise eigenvalue table
- comparison plots of the mode shapes

### 4. Bessel Functions

This page works with Bessel functions of the first kind for orders 0 and 1.

It includes:

- the Bessel differential equation
- the radial mode formula
- the zero condition
- the graph of `J0(x)` or `J1(x)`
- a table of positive zeros
- radial vibration mode plots

### 5. Applications

This page connects the mathematics to simple examples in:

- signal decomposition and reconstruction
- acoustics and circular membrane vibration

### 6. Error Analysis

This page checks the numerical quality of the computed results. It shows:

- boundary residuals for the Sturm-Liouville eigenfunctions
- coarse-grid versus fine-grid differences
- RMSE values for sampled eigenfunction curves
- residuals at the computed Bessel zeros

## Project Structure

```text
app.py
README.md
requirements.txt
modules/
  __init__.py
  bessel.py
  content.py
  error_analysis.py
  plots.py
  sturm.py
  utils.py
```

## Main Files

### `app.py`

This is the main Streamlit entry point. It handles:

- sidebar navigation
- user inputs
- formula display
- tables
- rendering Matplotlib figures in Streamlit

### `modules/sturm.py`

This file contains the closed-form Sturm-Liouville calculations:

- eigenvalues
- eigenfunctions
- boundary residuals

### `modules/bessel.py`

This file contains the Bessel-function calculations:

- `J0(x)` and `J1(x)`
- positive zeros
- radial mode curves
- zero residual checks

### `modules/error_analysis.py`

This file computes:

- Sturm-Liouville boundary-condition errors
- coarse-versus-fine sampling errors
- RMSE values
- Bessel zero residuals

### `modules/plots.py`

This file creates all graphs used by the app:

- eigenfunction plots
- eigenvalue trend plots
- Bessel-function plots
- radial mode plots
- error-analysis plots
- signal decomposition plots

### `modules/content.py`

This file stores the explanatory text shown in the app.

### `modules/utils.py`

This file contains shared helpers for:

- validation
- domain-grid creation
- radius-grid creation
- plot color settings

## Tech Stack

- Python 3.12
- Streamlit
- NumPy
- SciPy
- Matplotlib

## How To Install

Open a terminal in the project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks script execution, run this once in the same terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the virtual environment again:

```powershell
.\.venv\Scripts\Activate.ps1
```

## How To Run The Project

Run the Streamlit app with:

```powershell
python -m streamlit run app.py
```

If that does not work in your shell, use:

```powershell
.\.venv\Scripts\streamlit.exe run app.py
```

After running the command, Streamlit will print a local URL in the terminal. Open that URL in your browser.

## How To Use The Project

1. Start the app.
2. Open the local Streamlit link shown in the terminal.
3. Use the sidebar to switch between pages.
4. Change the inputs to update the tables and graphs.
5. Use the formulas, tables, and plots for your assignment.

## Inputs Available In The App

Depending on the page, the app lets you change:

- number of modes
- domain length `L`
- graph resolution
- Bessel order `0` or `1`
- Bessel x-range
- coarse and fine resolution for error analysis

## Mathematical Model Used

The Sturm-Liouville section uses:

- `y'' + lambda y = 0`
- `y(0) = 0`
- `y(L) = 0`
- `lambda_n = (n^2 pi^2) / L^2`
- `y_n(x) = sin(n pi x / L)`

The Bessel section uses:

- `x^2 y'' + x y' + (x^2 - n^2)y = 0`
- `R_n(r) = J_n(alpha_n r / a)`
- `J_n(alpha_k) = 0`

The error analysis includes:

- boundary residual checks
- maximum difference between coarse and fine sampling
- RMSE for interpolated curves
- absolute residual at each Bessel zero
