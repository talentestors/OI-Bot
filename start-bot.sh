#!/bin/bash
set -e

# Activate virtual environment
source .venv/bin/activate

# Execute the main application
exec python bot.py
