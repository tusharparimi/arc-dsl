import ast
import os
from collections import defaultdict
from typing import Dict, List, Tuple


import argparse


class FunctionSignatureExtractor(ast.NodeVisitor):
    def __init__(self):
        self.functions = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        func_name = node.name

        input_types = []
        for arg in node.args.args:
            annotation = self._annotation_to_string(arg.annotation)
            input_types.append((arg.arg, annotation))

        output_type = self._annotation_to_string(node.returns)

        self.functions.append(
            {
                "name": func_name,
                "inputs": input_types,
                "output": output_type,
            }
        )

        self.generic_visit(node)

    def _annotation_to_string(self, annotation):
        if annotation is None:
            return "Unknown"

        try:
            return ast.unparse(annotation)
        except Exception:
            return str(annotation)



def format_input_signature(inputs: List[Tuple[str, str]]) -> str:
    if not inputs:
        return "()"

    return "(" + ", ".join([f"{name}: {typ}" for name, typ in inputs]) + ")"



def build_hierarchy(functions: List[Dict]):
    hierarchy = defaultdict(lambda: defaultdict(list))

    for fn in functions:
        input_signature = format_input_signature(fn["inputs"])
        output_type = fn["output"]

        hierarchy[input_signature][output_type].append(fn["name"])

    return hierarchy



def write_output(hierarchy, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# ARC DSL Function Categorization\n\n")
        f.write(
            "Functions are grouped by input signature and then by output type in a single table.\n\n"
        )

        f.write("| Input Signature | Output Type | Functions |\n")
        f.write("|---|---|---|\n")

        for input_signature in sorted(hierarchy.keys()):
            outputs = hierarchy[input_signature]

            first_input_row = True

            for output_type in sorted(outputs.keys()):
                function_names = sorted(outputs[output_type])
                functions_str = ", ".join(
                    [f"`{fn}`" for fn in function_names]
                )

                input_cell = input_signature if first_input_row else ""

                f.write(
                    f"| `{input_cell}` | `{output_type}` | {functions_str} |\n"
                )

                first_input_row = False


def main():
    parser = argparse.ArgumentParser(
        description="Categorize ARC-DSL functions by input and output types"
    )

    parser.add_argument(
        "dsl_file",
        type=str,
        help="Path to dsl.py file"
    )

    parser.add_argument(
        "output_file",
        type=str,
        help="Path to output txt file"
    )

    args = parser.parse_args()

    dsl_file = args.dsl_file
    output_file = args.output_file

    if not os.path.exists(dsl_file):
        raise FileNotFoundError(
            f"Could not find '{dsl_file}'"
        )

    with open(dsl_file, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    extractor = FunctionSignatureExtractor()
    extractor.visit(tree)

    hierarchy = build_hierarchy(extractor.functions)

    write_output(hierarchy, output_file)

    print(f"Found {len(extractor.functions)} functions")
    print(f"Saved categorized output to: {output_file}")


if __name__ == "__main__":
    main()
