import sys
import importlib.util

def run_script(script_path):
    spec = importlib.util.spec_from_file_location("script", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

if __name__ == "__main__":
    script_path = './3-main.py'
    run_script(script_path)

