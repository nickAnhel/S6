import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(adj_matrix: list[list[int]]) -> None:
    edges = [(i, j, it) for i, row in enumerate(adj_matrix) for j, it in enumerate(row) if it]

    g = nx.Graph()
    g.add_nodes_from(range(5))

    for u, v, w in edges:
        g.add_edge(u, v, weight=w)

    pos = nx.spring_layout(g, seed=7)

    nx.draw_networkx_nodes(g, pos, node_size=700)
    nx.draw_networkx_edges(g, pos, edgelist=edges, width=1)

    nx.draw_networkx_labels(g, pos, font_size=20, font_family="sans-serif")

    edge_labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
