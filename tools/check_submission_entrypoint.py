#!/usr/bin/env python
from __future__ import annotations

import argparse
import ast
from pathlib import Path


def target_names(target: ast.expr) -> set[str]:
    if isinstance(target, ast.Name):
        return {target.id}
    if isinstance(target, (ast.Tuple, ast.List)):
        names: set[str] = set()
        for element in target.elts:
            names.update(target_names(element))
        return names
    return set()


def statement_bound_names(statement: ast.stmt) -> set[str]:
    if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return {statement.name}
    if isinstance(statement, (ast.Import, ast.ImportFrom)):
        return {
            alias.asname or alias.name.split(".", 1)[0]
            for alias in statement.names
        }
    if isinstance(statement, ast.Assign):
        names: set[str] = set()
        for target in statement.targets:
            names.update(target_names(target))
        return names
    if isinstance(statement, (ast.AnnAssign, ast.AugAssign)):
        return target_names(statement.target)
    if isinstance(statement, (ast.For, ast.AsyncFor)):
        names = target_names(statement.target)
        for child in statement.body + statement.orelse:
            names.update(statement_bound_names(child))
        return names
    if isinstance(statement, (ast.With, ast.AsyncWith)):
        names = set()
        for item in statement.items:
            if item.optional_vars is not None:
                names.update(target_names(item.optional_vars))
        for child in statement.body:
            names.update(statement_bound_names(child))
        return names
    if isinstance(statement, ast.If):
        names = set()
        for child in statement.body + statement.orelse:
            names.update(statement_bound_names(child))
        return names
    if isinstance(statement, (ast.While, ast.Try)):
        names = set()
        child_groups = [statement.body, statement.orelse]
        if isinstance(statement, ast.Try):
            child_groups.extend([statement.finalbody])
            child_groups.extend(handler.body for handler in statement.handlers)
        for group in child_groups:
            for child in group:
                names.update(statement_bound_names(child))
        return names
    return set()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="submission/main.py")
    args = parser.parse_args()

    path = Path(args.path)
    module = ast.parse(path.read_text())
    functions = [
        (index, node)
        for index, node in enumerate(module.body)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    if not functions:
        print("error: no top-level functions found")
        return 1

    function_index, function = functions[-1]
    print(f"last top-level function: {function.name}")

    earlier_names: set[str] = set()
    for statement in module.body[:function_index]:
        earlier_names.update(statement_bound_names(statement))
    if function.name in earlier_names:
        print(
            "error: final function name was bound earlier; redefining a global "
            "does not move it to the end of Kaggle's callable insertion order"
        )
        return 1

    later_names: set[str] = set()
    for statement in module.body[function_index + 1 :]:
        later_names.update(statement_bound_names(statement))
    if later_names:
        joined = ", ".join(sorted(later_names))
        print(
            "error: top-level names are bound after the final function "
            f"({joined}); Kaggle may select a later callable"
        )
        return 1

    print(f"loader-safe final function: {function.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
