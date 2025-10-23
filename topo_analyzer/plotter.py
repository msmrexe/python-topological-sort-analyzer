# topo_analyzer/plotter.py

"""
Handles the generation of all performance plots using Seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def generate_plots(df: pd.DataFrame, output_dir: str):
    """
    Generates and saves line plots for time complexity.
    
    Args:
        df: The DataFrame containing the analysis results.
        output_dir: The directory to save plot images to.
    """
    print(f"Generating plots in '{output_dir}'...")
    os.makedirs(output_dir, exist_ok=True)
    
    # Use a clean seaborn theme
    sns.set_theme(style="whitegrid")

    # --- Plot: Time Complexity vs. (V+E) ---
    plt.figure(figsize=(12, 7))
    
    # We use 'V+E' on the x-axis as this is the
    # true measure of input size for O(V+E) algorithms
    time_plot = sns.lineplot(
        data=df,
        x="V+E",
        y="Time (ms)",
        hue="Algorithm",
        style="Algorithm",
        markers=True,
        dashes=True
    )
    
    title = f"Topological Sort Performance (Time vs. V+E)"
    time_plot.set_title(title, fontsize=16)
    time_plot.set_xlabel("Graph Size (Nodes + Edges)", fontsize=12)
    time_plot.set_ylabel("Average Time (milliseconds)", fontsize=12)
    plt.legend(title="Algorithm")
    
    filename = "time_complexity_vs_v_plus_e.png"
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath)
    plt.close()

    print("All plots generated successfully.")
