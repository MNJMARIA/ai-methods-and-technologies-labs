# Lab 1 — Fuzzy sets and operations on them

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-arrays-013243)](https://numpy.org/)
[![scikit-fuzzy](https://img.shields.io/badge/scikit--fuzzy-fuzzy%20logic-green)](https://github.com/scikit-fuzzy/scikit-fuzzy)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-plots-orange)](https://matplotlib.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python script that builds fuzzy sets with different types of membership functions and performs the basic logical operations on them. Developed as the first lab work for the "Methods and Technologies of Artificial Intelligence" course (Software Engineering, Igor Sikorsky Kyiv Polytechnic Institute, 2026).

The script solves eight tasks. For each of them it computes the membership values with `scikit-fuzzy` and `NumPy`, draws the plot with `Matplotlib`, shows it on the screen, and saves it to the `img/` folder so that the figures can be inserted into the report. The parameters of every function are chosen freely, as the assignment allows.

Back to the [list of all labs](../README.md).

## Tasks and Results

| # | Task | Functions used | Figure |
|---|---|---|---|
| 1 | Triangular and trapezoidal membership functions | `trimf`, `trapmf` | [1_trimf_trapmf.png](img/1_trimf_trapmf.png) |
| 2 | Simple and two-sided Gaussian membership functions | `gaussmf`, `gauss2mf` | [2_gauss_gauss2.png](img/2_gauss_gauss2.png) |
| 3 | Generalized bell membership function | `gbellmf` | [3_gbellmf.png](img/3_gbellmf.png) |
| 4 | Set of sigmoid functions: basic one-sided (open left or right), two-sided, asymmetric | `sigmf`, `dsigmf`, `psigmf` | [4_sigmoid.png](img/4_sigmoid.png) |
| 5 | Polynomial functions (Z, PI, S) | `zmf`, `pimf`, `smf` | [5_zmf_pimf_smf.png](img/5_zmf_pimf_smf.png) |
| 6 | Minimax interpretation of fuzzy AND / OR | `numpy.fmin`, `numpy.fmax` | [6_minmax.png](img/6_minmax.png) |
| 7 | Probabilistic interpretation of fuzzy AND / OR | product, algebraic sum | [7_probabilistic.png](img/7_probabilistic.png) |
| 8 | Complement of a fuzzy set ("NOT A") | `1 − μ(x)` | [8_complement.png](img/8_complement.png) |

For tasks 6–8 two base sets are used: **A** = `gaussmf(x, 8, 2.5)` ("approximately 8") and **B** = `gaussmf(x, 12, 3)` ("approximately 12").

### What the operations mean

| Operation | Minimax | Probabilistic |
|---|---|---|
| Intersection (AND) | `min(μA, μB)` | `μA · μB` |
| Union (OR) | `max(μA, μB)` | `μA + μB − μA · μB` |
| Complement (NOT) | `1 − μA` | `1 − μA` |

The minimax result has a sharp break where the two curves cross, while the product and the algebraic sum give smoother curves. For the same sets the product is never greater than the minimum, and the algebraic sum is never smaller than the maximum.

## Folder Structure

```text
lab1_fuzzy_sets_formation_and_operations/
├── lab1.py                          # Solutions of all 8 tasks, step by step
├── img/                             # Figures saved by the script (created on first run)
├── requirements.txt                 # Python dependencies
└── README.md
```

## How to Run

1. Install Python 3 and create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   # Windows:  .venv\Scripts\activate
   # Linux/macOS:  source .venv/bin/activate
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   `scikit-fuzzy` needs `SciPy` and `NetworkX`, so all five packages are listed explicitly.

3. Run the script from this folder:

   ```bash
   python lab1.py
   ```

Each figure opens in its own window. The script continues to the next task when the window is closed. All 8 images are saved to `img/`.

## The Process

- Analysis of the assignment and of the lecture material on membership functions and operations on fuzzy sets
- Choice of the universe of discourse and of the parameters of each function (the values were chosen freely)
- Computation of membership values with `scikit-fuzzy` and `NumPy`
- Plots with `Matplotlib`: titles, axis labels, legends with the parameters of each set
- Checking the graphs against the theory: where the membership equals 1, where it equals 0.5, how the shape changes with the parameters
- Writing the report with the code, figures, and conclusions

## What I Learned

- What a **membership function** is and how its shape is set by parameters
- How the parameters change the graph: width and steepness of a bell, direction of a sigmoid, plateau of a trapezoid
- How a continuous universe is represented in code with `np.linspace` and why the number of points matters (the end points are included)
- The difference between the **minimax** and **probabilistic** interpretations of fuzzy AND / OR, and how it looks on a graph
- How the **complement** `1 − μ(x)` turns "approximately 8" into "not approximately 8"
- Working with `NumPy` arrays element by element, and drawing and saving figures with `Matplotlib`
- Setting up a Python virtual environment and managing dependencies

## How It Could Be Improved

- Add a function that draws any set of membership functions, to avoid repeated plotting code
- Add other fuzzy operators (Łukasiewicz, drastic, Hamacher)
- Add the characteristics of a fuzzy set: support, core, height, α-cut
- Add interactive sliders to change the parameters and see the shape change
- Add tests that check the key values (for example `trimf` equals 1 at its peak)

---

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---

**Author:** Mariia Stepanova  
**Program:** Software Engineering  
**Institution:** Igor Sikorsky Kyiv Polytechnic Institute (Kyiv, Ukraine)  
**Year:** 2026
