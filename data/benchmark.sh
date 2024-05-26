#!/bin/bash

# Directory containing the text files
dir="/home/khal/AIDS/Projekt3/AiDS-3/data/benchmark"

# Iterate over the text files in the directory
for file in "$dir"/*
do
    # Run the Python script with the -bst option and the text file as input
    python3 /home/khal/AIDS/Projekt3/AiDS-3/data/main.py --generate < "$file"
done