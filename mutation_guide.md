# Mutation Testing Report Guide

This guide explains how to run mutation testing and generate reports for your project.

## Prerequisites
Ensure you are in the project root (`/home/abhinav/Downloads/st_project`).

## 1. Full Project Mutation Testing (Recommended)
Since `tests.test_all_modules.py` contains tests for all utility modules, you can run mutation testing on the entire `src` package at once.

### Generate HTML Report
```bash
./.venv/bin/mut.py \
  --target src \
  --unit-test tests.test_all_modules \
  --operator AOR ROR CRP \
  --report-html mutation_reports/full_project \
  --path .
```

### Generate YAML Report
```bash
./.venv/bin/mut.py \
  --target src \
  --unit-test tests.test_all_modules \
  --operator AOR ROR CRP \
  --report full_project_report.yaml \
  --path .
```

## 2. Single Module Mutation Testing
If you want to test a specific module (e.g., `src.matrix_ops`) using the comprehensive test suite:

## 3. Integration Level Mutation Testing
To run mutation testing on the Banking System (integration level) and generate a report:

### Generate HTML Report

```bash
./.venv/bin/mut.py \
  --target src.banking \
  --unit-test tests.test_banking \
  --operator SDL LCR COD \
  --report-html mutation_reports/integration \
  --path .
```

### Generate YAML Report

```bash
./.venv/bin/mut.py \
  --target src.banking \
  --unit-test tests.test_banking \
  --operator SDL LCR COD \
  --report integration_report.yaml \
  --path .
```

## Explanation of Flags
- `--target`: The module to mutate (source code).
- `--unit-test`: The test module to run against the mutants.
- `--operator`: Specific mutation operators to apply.
    - **Unit Level**: `AOR` (Arithmetic), `ROR` (Relational), `CRP` (Constant Replacement).
    - **Integration Level**: `SDL` (Statement Deletion), `LCR` (Logical Connector), `COD` (Conditional Operator Deletion).
- `--report-html [DIR]`: Generates an HTML report in the specified directory.
- `--report [FILE]`: Generates a YAML report in the specified file.
- `--path .`: Adds the current directory to the Python path to resolve imports correctly.
