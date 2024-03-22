import subprocess
import re
from statistics import mean, median
import time


def run_command(command, iterations=10):
    times = []
    for _ in range(iterations):
        start_time = time.perf_counter()
        subprocess.run(command, shell=True)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        times.append(elapsed_time)
    return times


def compute_stats(times):
    return {
        "average": mean(times),
        "median": median(times),
        "min": min(times),
        "max": max(times),
    }


commands = {
    "Python": "python3 src/python.py",
    "Node": "node src/node.js",
    "Deno": "deno run --allow-read --allow-write src/deno.ts",
    "Bun": "bun run src/bun.ts",
}

results = {}

for runtime, command in commands.items():
    times = run_command(command)
    stats = compute_stats(times)
    print(stats)
    results[runtime] = stats

sorted_by_average = sorted(results.items(), key=lambda x: x[1]["average"])
sorted_by_min = sorted(results.items(), key=lambda x: x[1]["min"])

print("Sorted by Fastest Average:")
for runtime, stats in sorted_by_average:
    print(
        f"{runtime}: Avg = {stats['average']:.3f}s, Min = {stats['min']:.3f}s, Max = {stats['max']:.3f}s, Median = {stats['median']:.3f}s"
    )

print("\nSorted by Fastest Min:")
for runtime, stats in sorted_by_min:
    print(
        f"{runtime}: Min = {stats['min']:.3f}s, Avg = {stats['average']:.3f}s, Max = {stats['max']:.3f}s, Median = {stats['median']:.3f}s"
    )
