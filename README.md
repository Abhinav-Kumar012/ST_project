# CSE 731: Software Testing - Project Work

## Team Members
| Name | Roll Number |
|------|-------------|
| Abhinav Kumar | IMT2022079 |
| Aaditya Joshi | IMT2022092 |

## Project Overview
This project applies **mutation testing** to a large Python codebase (~1000+ LOC) consisting of algorithmic, mathematical, data-structure, utility, and integration modules.

The goal is to demonstrate:

* Strongly killing mutants at both **unit** and **integration** levels
* Use of **multiple mutation operators**
* Automated mutation analysis using open-source tools
* Clear mapping of test cases to mutation-based adequacy criteria

The codebase implements multiple complete functionalities spread across modules such as:

* Geometry computations (`geometry.py`)
* Banking operations (`banking.py`)
* Graph algorithms (`graph_algos.py`)
* Data-structure manipulation (`data_structures.py`)
* Searching, sorting, statistics, matrix operations
* End-to-end workflows in integration modules (`integration.py`, `integration_2.py`, `integration_3.py`)
* matrix operations (`matrix_ops.py`)
* search algorithms (`search_algos.py`)
* sorting algorithms (`sorting_algos.py`)
* string operations (`string_utils.py`)
* statistics (`stats_lib.py`)
* utility functions (`utils.py`)
* set operations (`set_ops.py`)

| folder | files | code |
|---------|-------|------|
| src | 15 | 1388 |
| tests | 15 | 1095 |

## Repository Link

A full version of the project and test suite is available at:

[https://github.com/Abhinav-Kumar012/ST_project.git](https://github.com/Abhinav-Kumar012/ST_project.git)

This repository contains:

* The `src/` and `tests/` folders
* Mutation testing configuration and scripts
* HTML reports for unit and integration mutation testing

## Source Code Description

The `src/` directory contains the following modules:

* **geometry.py** — distance, area, polygon checks, slope calculations
* **banking.py** — account operations, interest calculations, validations
* **graph_algos.py** — BFS, DFS, topological sort, shortest-path utilities
* **data_structures.py** — stack, queue, linked list primitives
* **matrix_ops.py** — matrix addition, multiplication, transformations
* **sorting_algos.py** —  merge, insertion, quick sort
* **search_algos.py** — linear search, binary search
* **set_ops.py** — set union, intersection, difference
* **string_utils.py** — snake case, camel case, palindrome, anagram
* **stats_lib.py** — mean, median, mode, variance computations
* **utils.py** — general helper functions
* **integration.py**, **integration_2.py**, **integration_3.py** — multi-module workflows combining utils, geometry, banking, stats_lib, string_utils, sorting_algos, search_algos, graph_algos, matrix_ops, set_ops


The integration modules are used specifically for **integration-level mutation testing**, as required in the project statement .

## Test Case Design Strategy (Mutation Testing)

We implemented a mutation-based test strategy for **unit testing** and **integration testing**, satisfying the project requirement of using mutation operators at both levels with strong mutant killing .For **unit testing**, we have tried using node coverage. 

### **Unit-Level Mutation Operators Used**

1. **Statement Deletion (SDL):** Deletes a statement to test if the missing logic is detected.
2. **Logical Connector Replacement (LCR):** Replaces logical connectors (e.g., `and` with `or`).
3. **Conditional Operator Deletion / Negation (COD):** Deletes a conditional operator.
4. **Conditional Operator Insertion (COI):** Adds Not statements to invert consitional statements.

### **Integration-Level Mutation Operators Used**
1.  **Statement Deletion (SDL):** Deletes a statement to test if the missing logic is detected.
2.  **Logical Connector Replacement (LCR):** Replaces logical connectors (e.g., `and` with `or`).
3.  **Relational Operator Replacement  (ROR):**  Replaces relational operators (e.g., `==` with `!=`).
4. **Conditional Operator Insertion (COI):** Adds Not statements to invert consitional statements.


## Tooling: `mut.py`
We are using `mut.py` for performing mutation testing. The `commands.sh` script demonstrates its usage.

### Setup
create a venv in the root directory and install the dependencies using the following command:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Usage
for indivisual module's report genration
```bash
mut.py --target src.utils --unit-test tests.test_utils_2 --operator SDL LCR COD --path . --report-html Reports/unit_utils
```

for full project report genration
```bash
bash commands.sh
```


### Explanation of Flags
- `--target`: The module to mutate (source code).
- `--unit-test`: The test module to run against the mutants.
- `--operator`: Specific mutation operators to apply.
- `--report-html [DIR]`: Generates an HTML report.
- `--path .`: Adds the current directory to the Python path.

## Individual Contributions
| Team Member | Contribution Details |
|-------------|----------------------|
| Abhinav Kumar | unit testing for banking, data_structures, graph_algos, matrix_ops,search_algos, utils, geometry,set_ops |
| Aaditya Joshi | integration testing and unit testing for sorting_algos, stats_lib, string_utils |