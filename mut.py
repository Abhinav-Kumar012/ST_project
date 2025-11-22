import argparse
import ast
import importlib
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
import yaml

# --- Mutation Operators ---

class MutationVisitor(ast.NodeTransformer):
    def __init__(self, operators):
        self.operators = operators
        self.mutations = []
        self.mutation_count = 0

    def visit_BinOp(self, node):
        if "AOR" in self.operators:
            # Arithmetic Operator Replacement
            replacements = {
                ast.Add: [ast.Sub, ast.Mult],
                ast.Sub: [ast.Add, ast.Mult],
                ast.Mult: [ast.Div, ast.Add],
                ast.Div: [ast.Mult, ast.Sub],
                ast.FloorDiv: [ast.Div],
                ast.Mod: [ast.Div],
                ast.Pow: [ast.Mult]
            }
            op_type = type(node.op)
            if op_type in replacements:
                for new_op in replacements[op_type]:
                    self.mutations.append({
                        "type": "AOR",
                        "node": node,
                        "replacement": ast.BinOp(left=node.left, op=new_op(), right=node.right),
                        "lineno": node.lineno
                    })
        return self.generic_visit(node)

    def visit_Compare(self, node):
        if "ROR" in self.operators:
            # Relational Operator Replacement
            replacements = {
                ast.Eq: [ast.NotEq],
                ast.NotEq: [ast.Eq],
                ast.Lt: [ast.Gt, ast.LtE],
                ast.LtE: [ast.GtE, ast.Lt],
                ast.Gt: [ast.Lt, ast.GtE],
                ast.GtE: [ast.LtE, ast.Gt],
                ast.Is: [ast.IsNot],
                ast.IsNot: [ast.Is],
                ast.In: [ast.NotIn],
                ast.NotIn: [ast.In]
            }
            # Only handle single comparisons for simplicity
            if len(node.ops) == 1:
                op_type = type(node.ops[0])
                if op_type in replacements:
                    for new_op in replacements[op_type]:
                        self.mutations.append({
                            "type": "ROR",
                            "node": node,
                            "replacement": ast.Compare(left=node.left, ops=[new_op()], comparators=node.comparators),
                            "lineno": node.lineno
                        })
        return self.generic_visit(node)

    def visit_Constant(self, node):
        if "CRP" in self.operators:
            # Constant Replacement
            if isinstance(node.value, (int, float)):
                self.mutations.append({
                    "type": "CRP",
                    "node": node,
                    "replacement": ast.Constant(value=node.value + 1),
                    "lineno": node.lineno
                })
                self.mutations.append({
                    "type": "CRP",
                    "node": node,
                    "replacement": ast.Constant(value=node.value - 1),
                    "lineno": node.lineno
                })
                if node.value != 0:
                     self.mutations.append({
                        "type": "CRP",
                        "node": node,
                        "replacement": ast.Constant(value=0),
                        "lineno": node.lineno
                    })
            elif isinstance(node.value, str):
                self.mutations.append({
                    "type": "CRP",
                    "node": node,
                    "replacement": ast.Constant(value="MUTATED"),
                    "lineno": node.lineno
                })
        return self.generic_visit(node)

    def visit_BoolOp(self, node):
        if "LCR" in self.operators:
            # Logical Connector Replacement
            if isinstance(node.op, ast.And):
                self.mutations.append({
                    "type": "LCR",
                    "node": node,
                    "replacement": ast.BoolOp(op=ast.Or(), values=node.values),
                    "lineno": node.lineno
                })
            elif isinstance(node.op, ast.Or):
                self.mutations.append({
                    "type": "LCR",
                    "node": node,
                    "replacement": ast.BoolOp(op=ast.And(), values=node.values),
                    "lineno": node.lineno
                })
        return self.generic_visit(node)

    # SDL (Statement Deletion) and COD (Conditional Operator Deletion) are harder with simple node replacement
    # because they involve removing or changing control flow structure.
    # We'll implement a simplified version.

    def visit_If(self, node):
        if "COD" in self.operators:
             # Conditional Operator Deletion - Negate condition
             self.mutations.append({
                "type": "COD",
                "node": node.test,
                "replacement": ast.UnaryOp(op=ast.Not(), operand=node.test),
                "lineno": node.lineno
            })
             # Force True
             self.mutations.append({
                "type": "COD",
                "node": node.test,
                "replacement": ast.Constant(value=True),
                "lineno": node.lineno
            })
             
        if "SDL" in self.operators:
            # Statement Deletion - Replace body with pass
            self.mutations.append({
                "type": "SDL",
                "node": node,
                "replacement": ast.If(test=node.test, body=[ast.Pass()], orelse=node.orelse),
                "lineno": node.lineno
            })
            
        return self.generic_visit(node)
    
    def visit_Assign(self, node):
        if "SDL" in self.operators:
             self.mutations.append({
                "type": "SDL",
                "node": node,
                "replacement": ast.Pass(),
                "lineno": node.lineno
            })
        return self.generic_visit(node)
        
    def visit_Expr(self, node):
        if "SDL" in self.operators:
             self.mutations.append({
                "type": "SDL",
                "node": node,
                "replacement": ast.Pass(),
                "lineno": node.lineno
            })
        return self.generic_visit(node)


def apply_mutation(tree, mutation):
    # Helper to apply a single mutation to the AST
    # We need a fresh transformer or a way to target the specific node
    # Since nodes don't have IDs, we'll use a location-based transformer
    
    class ApplyMutant(ast.NodeTransformer):
        def __init__(self, target_mutation):
            self.target_mutation = target_mutation
            self.applied = False

        def generic_visit(self, node):
            if self.applied:
                return super().generic_visit(node)
            
            if node == self.target_mutation["node"]:
                self.applied = True
                return self.target_mutation["replacement"]
            
            return super().generic_visit(node)
            
    applier = ApplyMutant(mutation)
    new_tree = applier.visit(tree)
    ast.fix_missing_locations(new_tree)
    return new_tree

def run_tests(test_module, timeout=5):
    # Run tests in a subprocess to ensure isolation
    cmd = [sys.executable, "-m", "unittest", test_module]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False # Treated as killed (or at least not survived)

def main():
    parser = argparse.ArgumentParser(description="Simple Mutation Testing Tool")
    parser.add_argument("--target", required=True, help="Target module to mutate")
    parser.add_argument("--unit-test", required=True, help="Test module to run")
    parser.add_argument("--operator", nargs="+", required=True, help="Mutation operators")
    parser.add_argument("--report-html", help="Directory for HTML report")
    parser.add_argument("--report", help="File for YAML report")
    parser.add_argument("--path", default=".", help="Path to project root")
    parser.add_argument("--timeout", type=int, default=5, help="Timeout for test execution in seconds")
    
    args = parser.parse_args()
    
    sys.path.insert(0, args.path)
    
    # Locate the target file
    try:
        target_spec = importlib.util.find_spec(args.target)
        if not target_spec or not target_spec.origin:
            print(f"Error: Could not find target module {args.target}")
            sys.exit(1)
        target_file = target_spec.origin
    except Exception as e:
        print(f"Error importing target: {e}")
        sys.exit(1)
        
    print(f"Mutating {args.target} ({target_file})")
    
    with open(target_file, "r") as f:
        source = f.read()
        
    tree = ast.parse(source)
    
    # Identify potential mutations
    visitor = MutationVisitor(args.operator)
    visitor.visit(tree)
    
    print(f"Found {len(visitor.mutations)} potential mutants.")
    
    results = []
    
    # Run baseline tests
    print("Running baseline tests...")
    if not run_tests(args.unit_test):
        print("Baseline tests failed! Cannot proceed with mutation testing.")
        sys.exit(1)
    print("Baseline tests passed.")
    
    start_time = time.time()
    
    # Apply mutations and run tests
    for i, mutation in enumerate(visitor.mutations):
        print(f"Running mutant {i+1}/{len(visitor.mutations)} ({mutation['type']} at line {mutation['lineno']})...", end="", flush=True)
        
        # Create mutated AST
        # We need to deepcopy or re-parse because AST is modified in place
        # Re-parsing is safer/easier for this simple script
        temp_tree = ast.parse(source)
        
        # We need to find the equivalent node in the new tree. 
        # Since we can't easily map objects, we'll use a slightly different approach for the visitor
        # to store path indices or just re-run the visitor and pick the i-th mutation.
        
        # Re-visit to find the i-th mutation's node in the fresh tree
        temp_visitor = MutationVisitor(args.operator)
        temp_visitor.visit(temp_tree)
        target_mutation = temp_visitor.mutations[i]
        
        mutated_tree = apply_mutation(temp_tree, target_mutation)
        
        # Write mutated code to file
        # We overwrite the original file temporarily! This is dangerous but effective for subprocess tests.
        # Make a backup first.
        backup_file = target_file + ".bak"
        shutil.copy2(target_file, backup_file)
        
        try:
            with open(target_file, "w") as f:
                f.write(ast.unparse(mutated_tree))
                
            # Run tests
            survived = run_tests(args.unit_test, timeout=args.timeout)
            
            if survived:
                print(" SURVIVED")
                results.append({
                    "id": i,
                    "type": mutation["type"],
                    "lineno": mutation["lineno"],
                    "status": "survived"
                })
            else:
                print(" KILLED")
                results.append({
                    "id": i,
                    "type": mutation["type"],
                    "lineno": mutation["lineno"],
                    "status": "killed"
                })
                
        except Exception as e:
            print(f" ERROR: {e}")
        finally:
            # Restore original file
            try:
                shutil.copy2(backup_file, target_file)
            except Exception as e:
                print(f"Error restoring file: {e}")
                
            # Retry removing backup file to handle Windows file locking
            for _ in range(5):
                try:
                    if os.path.exists(backup_file):
                        os.remove(backup_file)
                    break
                except PermissionError:
                    time.sleep(0.1)
            else:
                print(f"Warning: Could not remove backup file {backup_file}")
            
    duration = time.time() - start_time
    
    # Calculate score
    total = len(results)
    killed = sum(1 for r in results if r["status"] == "killed")
    score = (killed / total) * 100 if total > 0 else 0
    
    print(f"\nMutation Score: {score:.2f}% ({killed}/{total})")
    print(f"Duration: {duration:.2f}s")
    
    # Generate Reports
    report_data = {
        "target": args.target,
        "test_module": args.unit_test,
        "score": score,
        "total": total,
        "killed": killed,
        "survived": total - killed,
        "mutants": results
    }
    
    if args.report:
        with open(args.report, "w") as f:
            yaml.dump(report_data, f)
        print(f"YAML report saved to {args.report}")
        
    if args.report_html:
        os.makedirs(args.report_html, exist_ok=True)
        html_content = f"""
        <html>
        <head><title>Mutation Report: {args.target}</title></head>
        <body>
            <h1>Mutation Report for {args.target}</h1>
            <p>Score: {score:.2f}%</p>
            <p>Killed: {killed} / {total}</p>
            <table border="1">
                <tr><th>ID</th><th>Type</th><th>Line</th><th>Status</th></tr>
                {''.join(f'<tr style="background-color: {"#ffcccc" if r["status"] == "survived" else "#ccffcc"}"><td>{r["id"]}</td><td>{r["type"]}</td><td>{r["lineno"]}</td><td>{r["status"]}</td></tr>' for r in results)}
            </table>
        </body>
        </html>
        """
        with open(os.path.join(args.report_html, "index.html"), "w") as f:
            f.write(html_content)
        print(f"HTML report saved to {args.report_html}")

if __name__ == "__main__":
    main()
