#!/usr/bin/python3
import sys
import random

# Mapper for Monte Carlo Pi estimation:
# Input: single integer N per line (number of random points to generate)
# Output: for each mapper, emits "pi_estimate\tN\tinside_count"
# where N = total points sampled, inside_count = points inside unit circle (x² + y² ≤ 1)
# Small N: faster but less accurate. Large N: slower but more precise pi estimate
# Usage: echo "1000000" | python3 mapper.py | sort | python3 reducer.py
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        num_points = int(line)  # Number of random points to sample in unit square [0,1]x[0,1]
    except ValueError:
        raise ValueError(f"Invalid input line: '{line}'. Expected single integer N (points per mapper)")

    inside_count = 0
    for _ in range(num_points):
        x = random.random()
        y = random.random()
        # Count points inside unit circle: x² + y² ≤ 1 (quarter circle area = π/4)
        if x * x + y * y <= 1.0:
            inside_count += 1

    print(f"pi_estimate\t{num_points}\t{inside_count}")