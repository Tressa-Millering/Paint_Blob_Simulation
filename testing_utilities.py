#Authored by Tressa Millering

console_color_opts = ["\033[30m", "\033[31m", "\033[32m", "\033[34m"]

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
ANIMATE IN CONSOLE
FOR TESTING PURPOSES
WILL NOT ANIMATE CORRECTLY IF TKINTER WINDOW IS OPEN

\033[0m - resets color 
\033[H  - moves cursor to 1,1
"""
def console_animate(colors:list[list[int]], N:int):
    reset = "\033[0m"
    print("\033[H", end="", flush=True)
    for i in range(N):
        print("[", end="")
        for j in range(N):
            color = console_color_opts[colors[i][j]]
            print(f"{color}●{reset} ", end="")
        print("\b]")
    print()


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
FOR TESTING
Just prints a 2D array in multiple lines. Can give it a label too
"""
def print_array(array, length, label=""):
    print(label + (":" if (label != "") else ""))
    for _ in range(0, length):
        print(array[_])
    print("\n")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def plotGraph(results):
    """
    Expected results format:
    [
        {"x": 10, "lowest": 0, "average": 3.2, "highest": 8},
        {"x": 20, "lowest": 0, "average": 2.1, "highest": 6}
    ]
    """
    if len(results) == 0:
        return

    xs      = [item["x"]       for item in results]
    lows    = [item["lowest"]   for item in results]
    avgs    = [item["average"]  for item in results]
    highs   = [item["highest"]  for item in results]

    fig, ax = plt.subplots(figsize=(7, 5))

    # Lines
    ax.plot(xs, lows,  color="black", linewidth=1)
    ax.plot(xs, avgs,  color="black", linewidth=1)
    ax.plot(xs, highs, color="black", linewidth=1)

    # Markers — circle for lowest, square for average, triangle for highest
    ax.plot(xs, lows,  marker="o", linestyle="none", color="black", markersize=6, label="lowest")
    ax.plot(xs, avgs,  marker="s", linestyle="none", color="black", markersize=6, label="average")
    ax.plot(xs, highs, marker="^", linestyle="none", color="black", markersize=6, label="highest")

    ax.set_title("Batch Simulation Results")
    ax.set_xlabel("Simulation Input")
    ax.set_ylabel("Blob Count")
    ax.legend(loc="upper right")

    plt.tight_layout()
    plt.show()