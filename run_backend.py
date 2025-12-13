#!/usr/bin/env python3
"""
Script to run backend commands from the root directory.
This script adds the backend directory to the Python path so that imports work correctly.
"""
import sys
import os
import subprocess
from pathlib import Path

def run_backend_command():
    """Run a backend command by passing arguments to python."""
    if len(sys.argv) < 2:
        print("Usage: python run_backend.py <module> [args...]")
        print("Example: python run_backend.py src.services.ingestion_service")
        return 1

    module_or_script = sys.argv[1]

    # Add the backend/src directory to the Python path
    backend_src_path = Path(__file__).parent / "backend" / "src"
    sys.path.insert(0, str(backend_src_path))

    # Add the backend directory to the Python path as well
    backend_path = Path(__file__).parent / "backend"
    sys.path.insert(0, str(backend_path))

    # Change to the backend directory to run the command
    original_cwd = os.getcwd()
    os.chdir(backend_path)

    try:
        # Import and run the specified module
        if module_or_script.endswith('.py'):
            # If it's a .py file, run it as a script
            script_path = module_or_script
            result = subprocess.run([sys.executable, script_path] + sys.argv[2:])
        else:
            # If it's a module, run it with -m
            result = subprocess.run([sys.executable, "-m", module_or_script] + sys.argv[2:])
    finally:
        # Restore original working directory
        os.chdir(original_cwd)

    return result.returncode

if __name__ == "__main__":
    sys.exit(run_backend_command())