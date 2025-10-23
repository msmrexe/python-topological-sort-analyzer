# Topological Sort Analyzer

This project is a Python tool to implement, compare, and analyze the practical performance of the two primary algorithms for topological sorting:

1.  **DFS-based Sort:** The classic recursive, depth-first search approach.
2.  **Kahn's Algorithm:** The iterative, source-removal (or in-degree-based) approach.

Both algorithms are theoretically **$O(V+E)$**, but this project analyzes their *empirical* (real-world) performance. It generates random Directed Acyclic Graphs (DAGs) of increasing size, times both algorithms on the same graphs, and plots the results to visualize their performance characteristics.
The project was implemented as part of an Algorithms & Data Structures course.

## Features

* **Algorithm Implementations:** Provides robust, cycle-detecting implementations for both DFS-based sort and Kahn's algorithm.
* **Efficient Kahn's Algorithm:** Uses `collections.deque` for $O(1)$ queue operations, ensuring a true $O(V+E)$ runtime.
* **Random DAG Generation:** Includes a utility to generate random DAGs of specified sizes and densities for fair and scalable analysis.
* **Performance Plotting:** Uses `seaborn` and `matplotlib` to generate a `Time vs. V+E` plot, which is the most accurate way to compare $O(V+E)$ algorithms.
* **Data Export:** Saves all raw experiment data to a `.csv` file.
* **Modular Package:** Code is cleanly structured in a `topo_analyzer` package.

## Project Structure

```
topological-sort-analyzer/
├── .gitignore
├── LICENSE
├── README.md                # This documentation
├── requirements.txt         # Project dependencies
├── main.py                  # Main runnable script (CLI)
└── topo_analyzer/
    ├── __init__.py          # Makes 'topo_analyzer' a package
    ├── graph.py             # Graph class with random DAG generator
    ├── algorithms.py        # Implementations of DFS sort and Kahn's
    ├── analyzer.py          # The 'timeit' analysis runner
    └── plotter.py           # Plot generation logic
```

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/msmrexe/python-topological-sort-analyzer.git
    cd python-topological-sort-analyzer
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the analysis:**
    ```bash
    # Run with default settings (max 2000 nodes, 0.1 density)
    python main.py
    
    # Run a larger, denser analysis
    python main.py --max-nodes 5000 --steps 25 --density 0.2
    
    # Specify output files
    python main.py --csv my_data.csv --plots-dir my_plots
    ```
    After running, check the `plots/` directory for your `.png` graph and `topo_sort_results.csv` for the raw data.

---

## How the Algorithms Work

### 1. DFS (Depth-First Search) Based Sort

This algorithm uses the post-order traversal of a DFS.

* **Logic:**
    1.  Start a DFS traversal from an unvisited node.
    2.  Mark the node as "visiting" (to detect cycles).
    3.  Recursively call DFS on all its unvisited neighbors.
    4.  **After** all neighbors have been fully explored, add the current node to the *end* of a list (or the front of a stack).
    5.  Mark the node as "visited."
* **Cycle Detection:** If the DFS encounters a node that is already in the "visiting" state (i.e., in the current recursion stack), it has found a back-edge, which means a cycle exists.
* **Result:** The final list, when reversed, is a valid topological sort.

### 2. Kahn's Algorithm (Source-Removal)

This algorithm works by iteratively removing nodes that have no incoming edges.

* **Logic:**
    1.  Calculate the **in-degree** (count of incoming edges) for every node in the graph.
    2.  Create a queue (using `deque` for $O(1)$ pops) and add all nodes with an in-degree of `0` to it.
    3.  Initialize an empty list for the topological order.
    4.  **Loop:** While the queue is not empty:
        * Pop a node `u` from the queue and add it to the topological order list.
        * For each neighbor `v` of `u`:
            * Decrement the in-degree of `v`.
            * If the in-degree of `v` becomes `0`, add `v` to the queue.
* **Cycle Detection:** If the final topological order list contains *fewer* nodes than the total number of nodes in the graph, it means the loop terminated early because there was a cycle (which left nodes with an in-degree > 0).

---

## Performance Analysis: Theoretical vs. Empirical

### Theoretical Analysis ($O(V+E)$)

Both algorithms have the same, efficient linear time complexity of **$O(V+E)$**:

* **DFS-based Sort:** The DFS visits every vertex (node) and every edge exactly once. The work done at each step is constant. Total time: $O(V+E)$.
* **Kahn's Algorithm:**
    1.  Calculating all in-degrees requires traversing all edges: $O(E)$ (or $O(V+E)$).
    2.  Initializing the queue by checking all nodes: $O(V)$.
    3.  The main loop processes each vertex exactly once (when it's popped from the queue) and each edge exactly once (when it decrements its neighbor's in-degree).
    4.  Total time: $O(V+E) + O(V) = O(V+E)$.

### Empirical Analysis (The Plotted Results)

Despite having the same theoretical complexity, the plots  show that **Kahn's Algorithm is consistently faster than the DFS-based sort.**

This is a classic example of how theoretical bounds don't tell the whole story. The reasons for this practical difference (which your course text correctly identifies) are:

1.  **Python Recursion Overhead:** The DFS algorithm is recursive. Python has a relatively high overhead for function calls. For a deep, "stringy" graph, this can result in thousands of recursive calls, each adding a small amount of overhead that accumulates.
2.  **Iterative vs. Recursive:** Kahn's algorithm is iterative (it's just a `while` loop). Iterative code is almost always faster in Python than equivalent recursive code because it avoids the function call overhead.
3.  **Data Structures:** The (now efficient) Kahn's algorithm relies on a `deque`, which is a highly optimized C-based data structure in Python, making its $O(1)$ `append` and `popleft` operations extremely fast.

It should be noted that the shape of the graph matters. A very "wide" graph (low depth) might favor DFS, while a very "deep" graph (long chains) will heavily favor the iterative Kahn's algorithm. By testing on random DAGs, our analysis finds the average-case performance, which clearly shows Kahn's advantage.

---

## Author

Feel free to connect or reach out if you have any questions!

* **Maryam Rezaee**
* **GitHub:** [@msmrexe](https://github.com/msmrexe)
* **Email:** [ms.maryamrezaee@gmail.com](mailto:ms.maryamrezaee@gmail.com)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.
