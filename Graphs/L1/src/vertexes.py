from __future__ import annotations

from dataclasses import dataclass, field
from reprlib import recursive_repr

from constants import VERTEXES
from perfomance import get_average_exec_time


@dataclass
class Vertex:
    index: int
    name: str

    parents: list[Vertex] = field(default_factory=list)
    children: list[Vertex] = field(default_factory=list)

    incoming_weights: list[int] = field(default_factory=list)
    outgoing_weights: list[int] = field(default_factory=list)

    @recursive_repr()
    def __str__(self) -> str:
        return (
            f"{self.name}({self.index}) "
            f"parents: <{", ".join(repr(p) for p in self.parents)}> "
            f"children: <{", ".join(repr(c) for c in self.children)}> "
            f"incoming weights: <{", ".join([str(w) for w in self.incoming_weights])}> "
            f"outgoing weights: <{", ".join([str(w) for w in self.outgoing_weights])}>"
        )

    @recursive_repr()
    def __repr__(self) -> str:
        return f"{self.name}({self.index})"

    def __hash__(self) -> int:
        return hash((self.index, self.name))


def get_vertex_list(adj_matrix: list[list[int]]) -> list[Vertex]:
    vs = [Vertex(index=idx, name=name) for idx, name in VERTEXES.items()]

    for i, row in enumerate(adj_matrix):
        for j, w in enumerate(row):
            if w:
                vs[i].children.append(vs[j])
                vs[i].outgoing_weights.append(w)

                vs[j].parents.append(vs[i])
                vs[j].incoming_weights.append(w)

    return vs


def find_neighbors(
    idx: int,
    vertex_list: list[Vertex],
) -> list[str]:
    for v in vertex_list:
        if v.index == idx:
            return sorted([repr(it) for it in set(v.children + v.parents)])
    return []


def check_vertex_chain(
    vs: list[int],
    vertex_list: list[Vertex],
) -> bool:
    if len(vs) < 2:
        return True

    for i in range(len(vs) - 1):
        if vertex_list[vs[i + 1]] not in vertex_list[vs[i]].children:
            return False

    return True


def find_vertexes_with_greater_weight_sum(
    value: int,
    vertex_list: list[Vertex],
) -> list[int]:
    return [
        v.index
        for v in vertex_list
        if sum(v.incoming_weights + v.outgoing_weights) > value
    ]


def get_edges_count(
    vertex_list: list[Vertex],
) -> int:
    return sum(len(vertex.children) for vertex in vertex_list)


def test_perfomace(
    vertex_list: list[Vertex],
) -> dict[str, float]:
    return {
        "Find neighbors": get_average_exec_time(find_neighbors, 1, vertex_list),
        "Check vertex chain": get_average_exec_time(check_vertex_chain, [0, 1, 2, 3, 4, 6], vertex_list),
        "Find vertexes whoose sum of weights greater than value": get_average_exec_time(
            find_vertexes_with_greater_weight_sum, 3, vertex_list
        ),
        "Get edges count": get_average_exec_time(get_edges_count, vertex_list),
    }
