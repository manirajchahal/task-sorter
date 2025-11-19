#!/usr/bin/env bash
# Run the task categorizer from the folder this script is in
cd "$(dirname "$0")"
python3 categorize_tasks.py
