# topo_analyzer/analyzer.py

"""
Handles the empirical analysis of topological sort algorithms.
"""

import timeit
import pandas as pd
import numpy as np
from .graph import Graph
from .algorithms import ALGORITHM_MAP

def run_analysis(algo_names: list[str], node_counts: list[int], density: float) -> pd.DataFrame:
    """
    Runs time analysis for given algorithms over a range of
    graph sizes.
    
    Args:
        algo_names: List of algorithm names to test.
        node_counts: List of 'num_nodes' to test.
        density: The graph density to use for the random DAGs.
        
    Returns:
        A pandas DataFrame with the results.
    """
    results = []
    
    for n in node_counts:
        print(f"Analyzing for n = {n} nodes...")
        
        # Generate a single graph for this size
        graph = Graph.generate_random_dag(n, density)
        num_edges = graph.E
        v_plus_e = n + num_edges
        
        for name in algo_names:
            func = ALGORITHM_MAP[name]
            
            # --- Time Analysis ---
            # Use a lambda to pass the graph to the function
            # Number of runs is set low (e.g., 10) for
            # potentially large graphs
            num_runs = 10
            try:
                timer = timeit.timeit(lambda: func(graph), number=num_runs)
                time_avg_ms = (timer / num_runs) * 1000  # Avg ms
            except Exception as e:
                print(f"Error timing {name} at n={n}: {e}")
                time_avg_ms = None

            # Append results
            results.append({
                "Algorithm": name,
                "Nodes (V)": n,
                "Edges (E)": num_edges,
                "V+E": v_plus_e,
                "Time (ms)": time_avg_ms,
            })
            
    return pd.DataFrame(results)
