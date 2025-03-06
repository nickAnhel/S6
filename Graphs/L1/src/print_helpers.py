import prettytable


def print_commands_help() -> None:
    print(
        "Available commands",
        "help      (h)               -  See available commands",
        "draw      (d)   [filename]  -  Save graph reprsentation to image ('.png', '.jpg' or '.'jpeg')",
        "matrix    (mx)              -  Print adjacency matrix",
        "edges     (ed)              -  Print edges list",
        "vertexes  (vs)              -  Print vertexes list",
        sep="\n",
    )


def print_actions_help() -> None:
    print(
        "help            (h)                    -  See available actions",
        "find_neighbors  (fn)   [vertex-index]  -  Find vertex neighbors",
        "check_chain     (cc)   [vertexes]      -  Check vertexes forms chain",
        "find_vertexes   (fv)   [value]         -  Find vertexes whoose sum of weights greater than value",
        "count           (cnt)                  -  Count edges",
        "size            (s)                    -  Size of list of edges (bytes)",
        "test            (t)                    -  Test perfomance in all cases",
        sep="\n",
    )


def print_results(results: dict[str, float]) -> None:
    table = prettytable.PrettyTable()
    table.add_column("Test", [], align="l")
    table.add_column("Result", [], align="l")
    table.add_rows([(test, res) for test, res in results.items()])  # type: ignore
    print(table)
