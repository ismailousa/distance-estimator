import os
import sys

# Get the current directory (the directory containing this script)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the project's root directory to sys.path
project_root = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.insert(0, project_root)