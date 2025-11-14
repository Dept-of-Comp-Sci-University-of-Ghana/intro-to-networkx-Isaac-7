# group_network_analysis.py
# Assignment: Social Network Analysis of Student Group
# Author: Isaac Okai
# Lecturer: Dr. Ansah

import networkx as nx
import matplotlib.pyplot as plt

# Create directed graph
DG = nx.DiGraph()

# Define relationships
# Students all know each other (bidirectional)
# Students know the lecturer, but the lecturer does not personally know each student (one-way)

edges = [
    # Student - Student mutual relationships (two-way)
    ("Dominic", "Adams"), ("Adams", "Dominic"),
    ("Dominic", "Isaac"), ("Isaac", "Dominic"),
    ("Dominic", "Emmanuel"), ("Emmanuel", "Dominic"),
    ("Dominic", "Richard"), ("Richard", "Dominic"),
    
     ("Isaac", "Richard"), ("Richard", "Isaac"),
    ("Isaac", "Emmanuel"), ("Emmanuel", "Isaac"),
    ("Isaac", "Adams"), ("Adams", "Isaac"),

    ("Emmanuel", "Richard"), ("Richard", "Emmanuel"),
    ("Emmanuel", "Adams"), ("Adams", "Emmanuel"),

    ("Richard", "Adams"), ("Adams", "Richard"),

    # Students - Lecturer (one-way)
    ("Dominic", "Dr Ansah"),
    ("Isaac", "Dr Ansah"),
    ("Emmanuel", "Dr Ansah"),
    ("Richard", "Dr Ansah"),
    ("Adams", "Dr Ansah")
]

# Add edges
DG.add_edges_from(edges)

# Draw network
nx.draw(
    DG,
    node_color="yellow",
    node_size=1300,
    arrows=True,
    with_labels=True,
    font_color="black",
    font_size=9
)

# Show graph image
plt.show()
