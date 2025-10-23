# main.py

"""
Topological Sort Analyzer - CLI

Main entry point to run the topological sort analysis.
This script coordinates the analysis and plotting modules.
"""

import argparse
import numpy as np
from topo_analyzer.analyzer import run_analysis
from topo_analyzer.plotter import generate_plots

def main():
    """Parses CLI arguments and runs the analysis."""
    
    parser = argparse.ArgumentParser(
        description="Run a comparative analysis of topological sort algorithms."
    )
    parser.add_argument(
        '--max-nodes',
        type=int,
        default=2000,
        help="Maximum number of nodes to test (default: 2000)"
    )
    parser.add_argument(
        '--steps',
        type=int,
        default=20,
        help="Number of different graph sizes to test (default: 20)"
    )
    parser.add_argument(
        '--density',
        type=float,
        default=0.1,
        help="Graph density (0.0 to 1.0) for random DAGs (default: 0.1)"
    )
    parser.add_argument(
        '--csv',
        type=str,
        default="topo_sort_results.csv",
        help="Filename to save the raw CSV data (default: topo_sort_results.csv)"
    )
    parser.add_argument(
        '--plots-dir',
        type=str,
        default="plots",
        help="Directory to save the output plots (default: plots)"
    )
    args = parser.parse_args()
    
    # 1. Setup the experiment parameters
    node_counts = np.linspace(start=50, stop=args.max_nodes, num=args.steps, dtype=int).tolist()
    
    algo_names = [
        "DFS-based Sort",
        "Kahn's Algorithm",
    ]
    
    print("--- Starting Topological Sort Analysis ---")
    print(f"Algorithms: {', '.join(algo_names)}")
    print(f"Node Counts: {node_counts}")
    print(f"Graph Density: {args.density}")
    
    # 2. Run the analysis
    df = run_analysis(algo_names, node_counts, args.density)
    
    # 3. Save the raw data
    df.to_csv(args.csv, index=False)
    print(f"\nRaw results saved to '{args.csv}'")
    
    # 4. Generate plots
    generate_plots(df, args.plots_dir)
    
    print("--- Analysis Complete ---")

if __name__ == "__main__":
    main()
