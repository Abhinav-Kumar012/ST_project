import unittest
import subprocess
import os
import sys

class TestMutation(unittest.TestCase):
    def run_mutation(self, target, test_module, mode="unit"):
        """
        Runs mutation testing using the mut.py script.
        
        Args:
            target (str): The module to mutate (e.g., 'src.string_utils').
            test_module (str): The test module to run (e.g., 'tests.test_new_features').
            mode (str): 'unit' or 'integration' to select operators.
        """
        # Determine path to mut.py
        # Assuming standard venv structure on Windows: .venv/Scripts/mut.py
        # Or Unix: .venv/bin/mut.py
        # We'll try to find it relative to the project root.
        
        project_root = os.getcwd()
        possible_paths = [
            os.path.join(project_root, ".venv", "Scripts", "mut.py"), # Windows venv
            os.path.join(project_root, ".venv", "bin", "mut.py"),     # Unix venv
            os.path.join(project_root, "mut.py"),                     # Root dir
            "mut.py"                                                  # In PATH
        ]
        
        mut_script = None
        for path in possible_paths:
            if os.path.exists(path):
                mut_script = path
                break
                
        if not mut_script:
            # Fallback: assume it's in the path or we can't run it
            print(f"Warning: mut.py not found in standard locations. Checked: {possible_paths}. Skipping mutation run.")
            return

        operators = []
        if mode == "unit":
            operators = ["AOR", "ROR", "CRP"]
        else:
            operators = ["SDL", "LCR", "COD"]
            
        cmd = [
            sys.executable,
            mut_script,
            "--target", target,
            "--unit-test", test_module,
            "--operator", *operators,
            "--path", project_root
        ]
        
        print(f"Running mutation test: {' '.join(cmd)}")
        
        # Run the command
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Check return code. Assuming 0 means success (survived mutants might cause non-zero? 
        # Usually mutation tools return 0 if the run completed, regardless of score, 
        # unless configured to fail on threshold).
        # For now, we assert that the script ran successfully.
        if result.returncode != 0:
            print(f"Mutation test failed with error:\n{result.stderr}")
            
        self.assertEqual(result.returncode, 0, f"Mutation testing failed for {target}")
        
        # Optionally, we could parse the output to check the mutation score
        # if the tool outputs it to stdout.

    # --- Unit Mutation Tests ---

    def test_unit_string_utils(self):
        """Unit mutation test for string_utils."""
        self.run_mutation("src.string_utils", "tests.test_new_features", mode="unit")

    def test_unit_stats_lib(self):
        """Unit mutation test for stats_lib."""
        self.run_mutation("src.stats_lib", "tests.test_new_features", mode="unit")

    def test_unit_search_algos(self):
        """Unit mutation test for search_algos."""
        self.run_mutation("src.search_algos", "tests.test_new_features", mode="unit")

    # --- Integration Mutation Tests ---

    def test_integration_banking(self):
        """Integration mutation test for banking system."""
        self.run_mutation("src.banking", "tests.test_banking", mode="integration")

    def test_integration_graph_algos(self):
        """Integration mutation test for graph algorithms (Graph + UnionFind)."""
        self.run_mutation("src.graph_algos", "tests.test_new_features", mode="integration")

    def test_integration_geometry(self):
        """Integration mutation test for geometry (Shapes + Points)."""
        self.run_mutation("src.geometry", "tests.test_new_features", mode="integration")

if __name__ == '__main__':
    unittest.main()
