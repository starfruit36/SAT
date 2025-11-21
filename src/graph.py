import networkx as nx
import cnf_parser
from itertools import combinations
SAT, num_of_var, num_of_clauses = cnf_parser.parse_dimacs("test.cnf")
G = nx.Graph()
combination = combinations
edges = []
G.add_nodes_from(range(1, num_of_var + 1))
for clause in SAT:
    for i in clause:
        if i > 0:
            edges.append(i)
        elif i < 0:
            edges.append(abs(i))
    connection = (combination(edges,2))
    edges.clear()
    for i in connection:
        G.add_edge(*i)

"""
[1, 2, -3]	(1, 2), (1, 3), (2, 3)	
[-3, 4]	(3, 4)	
"""