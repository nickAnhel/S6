from constants import VERTEXES
from perfomance import get_average_exec_time


def find_neighbors(
    idx: int,
    adj_matrix: list[list[int]],
) -> list[str]:
    from_vs = [i for i, it in enumerate(adj_matrix[idx]) if it]
    to_vs = [i for i, it in enumerate(adj_matrix) if it[idx]]
    return [VERTEXES[it] for it in set(from_vs + to_vs)]


def check_vertex_chain(
    vs: list[int],
    adj_matrix: list[list[int]],
) -> bool:
    if len(vs) < 2:
        return True

    for i in range(len(vs) - 1):
        if not adj_matrix[vs[i]][vs[i + 1]]:
            return False

    return True


def find_vertexes_with_greater_weight_sum(
    value: int,
    adj_matrix: list[list[int]],
) -> list[int]:
    result = []

    for i, row in enumerate(adj_matrix):
        outgoing_sum = sum(row)
        incoming_sum = sum(row[i] for row in adj_matrix)

        if outgoing_sum + incoming_sum > value:
            result.append(i)

    return result


def get_edges_count(
    adj_matrix: list[list[int]],
) -> int:
    return sum(
        sum(1 for _, w in enumerate(row) if w)
        for _, row in enumerate(adj_matrix)
    )


def test_perfomace(
    adj_matrix: list[list[int]],
) -> dict[str, float]:
    return {
        "Find neighbors": get_average_exec_time(find_neighbors, 1, adj_matrix),
        "Check vertex chain": get_average_exec_time(check_vertex_chain, [0, 1, 2, 3, 4, 6], adj_matrix),
        "Find vertexes whoose sum of weights greater than value": get_average_exec_time(
            find_vertexes_with_greater_weight_sum, 3, adj_matrix
        ),
        "Get edges count": get_average_exec_time(get_edges_count, adj_matrix),
    }
