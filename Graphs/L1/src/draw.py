import os
from pathlib import Path

import igraph as ig

from constants import ALLOWED_IMAGE_EXTENTIONS, VERTEX_NAMES


def _create_graph(adj_matrix: list[list[int]]) -> ig.Graph:
    graph = ig.Graph.Weighted_Adjacency(
        adj_matrix,
        mode=ig.ADJ_DIRECTED,
        attr="weight",
        loops="ignore",
    )
    graph.vs["label"] = VERTEX_NAMES

    return graph


def _is_image_path(p: Path) -> bool:
    basename = os.path.basename(p)
    _, ext = os.path.splitext(basename)

    if not ext or ext not in ALLOWED_IMAGE_EXTENTIONS:
        return False

    return True


def _save_image(plt, fpath: Path) -> None:
    if not _is_image_path(fpath):
        fpath = fpath / "graph.png"

    if not os.path.exists(fpath.parent):
        os.makedirs(fpath.parent)

    plt.save(fpath)


def save_graph(fpath: Path, adj_matrix: list[list[int]]) -> Path:
    graph = _create_graph(adj_matrix)

    plt = ig.plot(
        graph,
        bbox=(300, 300),
        vertex_label_color="black",
        vertex_label_size=10,
        vertex_size=20,
        vertex_color="white",
        edge_label=[int(w) for w in graph.es["weight"]],
        layout=graph.layout("kk"),
    )

    _save_image(plt, fpath)
    return fpath
