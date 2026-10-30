# AI Methods and Technologies — Lab Works Collection

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-arrays-013243)](https://numpy.org/)
[![scikit-fuzzy](https://img.shields.io/badge/scikit--fuzzy-fuzzy%20logic-green)](https://github.com/scikit-fuzzy/scikit-fuzzy)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-plots-orange)](https://matplotlib.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Collection of lab works for the "Methods and Technologies of Artificial Intelligence" course (Software Engineering, Igor Sikorsky Kyiv Polytechnic Institute, 2026).

Every lab is stored in its own folder with the source code, the figures it produces, the written report, and a detailed README. Labs are written in Python and do not depend on each other.

## Labs

| # | Lab | Description | Source |
|---|---|---|---|
| 1 | **Fuzzy sets and operations on them** | Building membership functions of different types (triangular, trapezoidal, Gaussian, generalized bell, sigmoid, polynomial) and performing the minimax and probabilistic interpretations of fuzzy AND / OR, plus the complement | [lab1_fuzzy_sets_formation_and_operations/](lab1_fuzzy_sets_formation_and_operations/) |

New labs are added to this table as they are completed.

## Technologies

- **Python 3**
- **NumPy** — arrays of membership values
- **scikit-fuzzy** — ready-made membership functions
- **SciPy** and **NetworkX** — dependencies of scikit-fuzzy
- **Matplotlib** — plots and saved figures

## Repository Structure

```text
ai-methods-and-technologies-labs/
├── README.md
└── lab1_fuzzy_sets_formation_and_operations/            # Lab 1 — fuzzy sets and operations on them
    ├── lab1.py
    ├── img/                    # 8 figures produced by lab1.py
    ├── requirements.txt
    └── README.md
```

Each lab is self-contained: it has its own script, figures, and README, so labs can be run or deleted independently.

## How to Run

```bash
git clone https://github.com/MNJMARIA/ai-methods-and-technologies-labs.git
cd ai-methods-and-technologies-labs/lab1_fuzzy_sets_formation_and_operations

python -m venv .venv
# Windows:  .venv\Scripts\activate
# Linux/macOS:  source .venv/bin/activate

pip install -r requirements.txt
python lab1.py
```

Every lab folder has its own `lab1_fuzzy_sets_formation_and_operations/requirements.txt` and its own run instructions in its README.

## How to Add a New Lab

1. Create a folder named `lab<number>_<topic>/` (for example `lab2_...`) with the script, a `lab1_fuzzy_sets_formation_and_operations/requirements.txt` if new packages are needed, and an `img/` folder for results.
2. Add a short `README.md` to the lab folder.
3. Add a new row to the table above and update the repository structure.
4. Commit and push.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Author:** Mariia Stepanova  
**Program:** Software Engineering  
**Institution:** Igor Sikorsky Kyiv Polytechnic Institute (Kyiv, Ukraine)  
**Year:** 2026
