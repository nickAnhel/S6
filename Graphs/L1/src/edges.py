from dataclasses import dataclass
from collections import defaultdict

from constants import VERTEXES
from perfomance import get_average_exec_time


@dataclass
class Edge:
    from_vertex: int
    to_vertex: int
    weight: int

    def __str__(self) -> str:
        return f"({self.from_vertex}) - {self.weight} -> ({self.to_vertex})"

    def __repr__(self) -> str:
        return f"<Edge: {str(self)}>"


def get_edges_list(adj_matrix: list[list[int]]) -> list[Edge]:
    return [
        Edge(
            from_vertex=i,
            to_vertex=j,
            weight=w,
        )
        for i, row in enumerate(adj_matrix)
        for j, w in enumerate(row)
        if w
    ]


def find_neighbors(
    idx: int,
    edges: list[Edge],
) -> list[str]:
    from_vs = [e.to_vertex for e in edges if e.from_vertex == idx]
    to_vs = [e.from_vertex for e in edges if e.to_vertex == idx]
    return [VERTEXES[v] for v in set(from_vs + to_vs)]


def check_vertex_chain(
    vs: list[int],
    edges: list[Edge],
) -> bool:
    if len(vs) < 2:
        return True

    pairs = [(e.from_vertex, e.to_vertex) for e in edges]
    for i in range(len(vs) - 1):
        if (vs[i], vs[i + 1]) not in pairs:
            return False

    return True


def find_vertexes_with_greater_weight_sum(
    value: int,
    edges: list[Edge],
) -> list[int]:
    vw = defaultdict(int)

    for edge in edges:
        vw[edge.from_vertex] += edge.weight
        vw[edge.to_vertex] += edge.weight

    return sorted([v for v, total_weight in vw.items() if total_weight > value])


def get_edges_count(
    edges: list[Edge],
) -> int:
    return len(edges)


def test_perfomace(
    edges: list[Edge],
) -> dict[str, float]:
    return {
        "Find neighbors": get_average_exec_time(find_neighbors, 1, edges),
        "Check vertex chain": get_average_exec_time(check_vertex_chain, [0, 1, 2, 3, 4, 6], edges),
        "Find vertexes whoose sum of weights greater than value": get_average_exec_time(
            find_vertexes_with_greater_weight_sum, 3, edges
        ),
        "Get edges count": get_average_exec_time(get_edges_count, edges),
    }
