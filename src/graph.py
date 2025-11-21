import networkx as nx
from itertools import combinations
def build_graph(num_of_var, clauses):
    G = nx.Graph()
    # 1. Add all nodes 
    G.add_nodes_from(range(1, num_of_var + 1))
    # 2. Add edges (Clique logic)
    for clause in clauses:
        clause_vars = [abs(x) for x in clause]
        for i in combinations(clause_vars, 2):
            G.add_edge(*i)
    return G