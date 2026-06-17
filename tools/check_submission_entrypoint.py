#!/usr/bin/env python
from __future__ import annotations

import argparse
import ast
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="submission/main.py")
    args = parser.parse_args()

    path = Path(args.path)
    module = ast.parse(path.read_text())
    functions = [node.name for node in module.body if isinstance(node, ast.FunctionDef)]
    if not functions:
        print("error: no top-level functions found")
        return 1
    last = functions[-1]
    print(f"last top-level function: {last}")
    if last != "agent":
        print("error: final top-level function must be agent")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
