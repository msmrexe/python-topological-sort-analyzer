# topo_analyzer/graph.py

"""
Contains a simple Graph class for representing
a Directed Acyclic Graph (DAG).
"""

import random
from collections import defaultdict

class Graph:
    """Represents a directed graph."""
    
    def __init__(self):
        self.adj = defaultdict(list)
        self._nodes = set()

    @property
    def V(self) -> int:
        """Number of vertices (nodes)."""
        return len(self._nodes)
    
    @property
    def E(self) -> int:
        """Number of edges."""
        return sum(len(adj_list) for adj_list in self.adj.values())

    def add_node(self, node: int):
        """Adds a node to the graph."""
        self._nodes.add(node)
        
    def add_edge(self, u: int, v: int):
        """Adds a directed edge from u to v."""
        self.adj[u].append(v)
        self._nodes.add(u)
        self._nodes.add(v)

    def get_all_nodes(self) -> set:
        """Returns a set of all nodes."""
        return self._nodes
        
    @classmethod
    def generate_random_dag(cls, num_nodes: int, density: float):
        """
        Generates a random Directed Acyclic Graph (DAG).
        
        Args:
            num_nodes: The number of nodes (vertices).
            density: A float (0.0 to 1.0) representing the
                     probability of an edge existing.
        """
        g = cls()
        nodes = list(range(num_nodes))
        
        for u in nodes:
            g.add_node(u)
            # Only add edges from a node 'u' to a node 'v'
            # where v > u. This guarantees no cycles.
            for v in range(u + 1, num_nodes):
                if random.random() < density:
                    g.add_edge(u, v)
        return g
