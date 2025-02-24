#!/bin/bash

# Navigate to the project directory
cd ~/Documents/GitHub/GCP-SkillTracker

# Activate the virtual environment
source venv/bin/activate

# Navigate to dev_notes
cd dev_notes

# Run Streamlit on port 8080
python -m streamlit run private.py --server.headless=true --server.port 8599
