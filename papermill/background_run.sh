#!/bin/bash

# Background run of the Jupyter notebook using Papermill in a dockerized environment with FacsimiLab

# Setup
#------------------------
cd /home/coder/work/protocol-timer

source /opt/conda/bin/activate

# Default notebook path
default_notebook_path="protocols/histology/Deparaffinization.ipynb"

# Prompt user for the notebook file path
echo "Available notebooks under ./protocols directory:"
find ./ -type d -name "env" -prune -o -type f -name "*.ipynb" -printf "%P\n"

# Prompt user for the notebook file path with a 5-second timeout
echo "Enter the path to the notebook file (default: $default_notebook_path): "
IFS= read -t 5 -r notebook_path || notebook_path="$default_notebook_path"

# Extract directory path from the notebook path
notebook_dir=$(dirname "$notebook_path")
echo "Directory name is $notebook_dir"

# Change directory to the notebook's directory
cd "$notebook_dir" || { echo "Error: Unable to change directory to $notebook_dir" >&2; exit 1; }

only_filename=$(basename "$notebook_path")

echo "Filename is $only_filename"

# Run
#------------------------
echo 'Started at ' $(date +"%F-%H-%M-%S")
echo '----------------------------------'

papermill "$only_filename" \
    "../../papermill/output/${only_filename}_output.ipynb" \
    --progress-bar \

# Complete
#------------------------
T="$(date +%s)"
echo '------------------------------------------------'
echo 'Ended at ' $(date +"%F-%H-%M-%S")
echo "It took $((($(date +%s)-T) / 60)) minutes to complete" 
echo ""
echo "Done."
