#!/usr/bin/python3
import sys
import random

# Mapper: read desired number of Monte Carlo samples (points) from stdin.
# Each input line is expected to contain a single integer N, where:
#   - N is the number of random points to generate in the unit square [0, 1] × [0, 1].
#   - Larger N gives a more accurate estimate of π but takes longer to compute.
#   - Smaller N runs faster but yields a noisier estimate.
#
# For each line, the mapper:
#   1. Generates N random points (x, y) uniformly in [0, 1] × [0, 1].
#   2. Counts how many of these points fall inside the quarter unit circle x² + y² ≤ 1.
#   3. Emits a single summary line: key, total_points, inside_circle_points.

for line in sys.stdin:
    line = line.strip()
    if not line:
        # Empty line is considered invalid input.
        # Fail fast so the user can fix the input rather than silently guessing.
        raise ValueError("Empty input line for number of points per mapper.")

    try:
        num_points = int(line)
    except ValueError:
        # Do not silently substitute a default, as this hides input problems.
        # Instead, raise an exception so the user can correct the corrupted input.
        raise ValueError(f"Invalid integer for number of points per mapper: {line!r}")

    if num_points <= 0:
        # Non‑positive values do not make sense for a sample size.
        raise ValueError(f"Number of points per mapper must be positive, got {num_points}.")

    # inside_count counts how many points fall inside the quarter unit circle
    # x^2 + y^2 <= 1 within the unit square [0, 1] × [0, 1].
    inside_count = 0
    for _ in range(num_points):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1.0:
            inside_count += 1

    # Emit: key    total_points    inside_circle_points
    print(f"pi_estimate\t{num_points}\t{inside_count}")
