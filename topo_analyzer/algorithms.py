# topo_analyzer/algorithms.py

"""
Contains the two primary algorithms for topological sorting:
1. DFS (Depth-First Search) based
2. Kahn's Algorithm (Source-Removal)
"""

from collections import deque, defaultdict
from .graph import Graph

class CycleDetectedError(ValueError):
    """Custom exception for graph cycles."""
    pass

def dfs_sort(graph: Graph) -> list[int]:
    """
    Performs a topological sort using a DFS-based algorithm.
    Includes cycle detection.
    
    Raises:
        CycleDetectedError: If the graph contains a cycle.
    """
    
    stack = []
    visited = set()
    recursion_stack = set() # For cycle detection
    
    def _dfs_visit(node):
        visited.add(node)
        recursion_stack.add(node)
        
        for neighbor in graph.adj[node]:
            if neighbor not in visited:
                _dfs_visit(neighbor)
            elif neighbor in recursion_stack:
                # We've found a back-edge
                raise CycleDetectedError("Graph contains a cycle.")
                
        # All neighbors visited, add node to *front* of list
        # (or append and reverse at end)
        stack.append(node)
        recursion_stack.remove(node)

    # Call _dfs_visit for all nodes
    for node in graph.get_all_nodes():
        if node not in visited:
            _dfs_visit(node)
            
    return stack[::-1] # Return the reversed stack

def kahn_sort(graph: Graph) -> list[int]:
    """
    Performs a topological sort using Kahn's algorithm
    (source-removal).
    
    Raises:
        CycleDetectedError: If the graph contains a cycle.
    """
    
    # 1. Calculate all in-degrees
    in_degree = {node: 0 for node in graph.get_all_nodes()}
    for node in graph.get_all_nodes():
        for neighbor in graph.adj[node]:
            in_degree[neighbor] += 1
            
    # 2. Initialize the queue with all 0-in-degree nodes
    # Use collections.deque for O(1) popleft()
    queue = deque([node for node in graph.get_all_nodes() if in_degree[node] == 0])
    
    topo_order = []
    node_count = 0
    
    # 3. Process the queue
    while queue:
        u = queue.popleft() # O(1) operation
        topo_order.append(u)
        node_count += 1
        
        for v in graph.adj[u]:
            in_degree[v] -= 1
            # If neighbor now has 0 in-degree, add to queue
            if in_degree[v] == 0:
                queue.append(v)
                
    # 4. Check for cycles
    if node_count != graph.V:
        raise CycleDetectedError("Graph contains a cycle.")
        
    return topo_order

# Map to access algorithms by name
ALGORITHM_MAP = {
    "DFS-based Sort": dfs_sort,
    "Kahn's Algorithm": kahn_sort,
}
