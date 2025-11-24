import matplotlib.pyplot as plt
import networkx as nx
def visualize_static_graph(G):
    #Plots the graph structure.
    plt.figure(figsize=(10, 8))

    # 1. Calculate Layout (The Physics Engine)
    pos = nx.spring_layout(G, k=0.5, seed=42)
    
    # 2. Draw the Graph
    nx.draw(G, pos,
            with_labels=True,  # Show Node IDs
            node_color='lightblue',
            node_size=600,
            font_weight='bold',
            edge_color='gray')
    
    # 3. Formatting
    plt.title("SAT Variable Interaction Graph")
    plt.axis('off')  # Hide the X/Y axis rulers
    plt.show()
