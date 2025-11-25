## Explanation of Flags
- `--target`: The module to mutate (source code).
- `--unit-test`: The test module to run against the mutants.
- `--operator`: Specific mutation operators to apply.
    - **Unit Level**: `AOR` (Arithmetic), `ROR` (Relational), `CRP` (Constant Replacement).
    - **Integration Level**: `SDL` (Statement Deletion), `LCR` (Logical Connector), `COD` (Conditional Operator Deletion).
- `--report-html [DIR]`: Generates an HTML report in the specified directory.
- `--report [FILE]`: Generates a YAML report in the specified file.
- `--path .`: Adds the current directory to the Python path to resolve imports correctly.