#!/usr/bin/python3
import sys
import random

# Mapper: Generate random points in unit square [0,1]x[0,1] and emit 1 if inside unit circle
# Input: single integer N per mapper (number of Monte Carlo samples to generate)
# Small N: faster but less accurate; large N: slower but more accurate pi estimate
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # Read number of Monte Carlo samples per mapper
    try:
        num_points = int(line)
    except ValueError:
        raise ValueError(f"Invalid input line '{line}': expected single integer N (number of Monte Carlo samples)")

    inside_count = 0  # Count of points inside unit circle (x^2 + y^2 <= 1)
    for _ in range(num_points):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1.0:
            inside_count += 1

    # Emit total points and inside points as key-value
    print(f"pi_estimate\t{num_points}\t{inside_count}")
