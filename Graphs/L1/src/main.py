import os
import sys
import datetime
from pathlib import Path

import prettytable

import draw
import matrix
import edges
import vertexes
from constants import ADJ_MATRIX, VERTEX_NAMES
from history import input_with_history
from print_helpers import print_commands_help, print_actions_help, print_results


BASE_DIR = Path(__file__).parent.parent


def main() -> None:
    os.system("clear")

    print(
        f"L1 v0.1.0 [{datetime.datetime.now()}] on {sys.platform}",
        "Type 'help' to see available commands",
        sep="\n",
    )

    eds = edges.get_edges_list(ADJ_MATRIX)
    vertex_list = vertexes.get_vertex_list(ADJ_MATRIX)

    while (command := input_with_history()) not in ("q", "e", "exit", "exit()"):
        match command.split():
            # System
            case ["help" | "h"]:
                print_commands_help()

            case ["clear" | "cls" | "c"]:
                os.system("clear")
                continue

            # Draw
            case ["draw" | "d"]:
                fpath = BASE_DIR / "images"
                image_path = draw.save_graph(fpath, ADJ_MATRIX)
                print(f"Graph reprsentation saved to {image_path!s}")

            case ["draw" | "d", filename]:
                fpath = BASE_DIR / "images" / filename
                image_path = draw.save_graph(fpath, ADJ_MATRIX)
                print(f"Graph reprsentation saved to {image_path!s}")

            # Adjacency matrix
            case ["matrix" | "mx"]:
                table = prettytable.PrettyTable([""] + VERTEX_NAMES)
                table.add_rows([[VERTEX_NAMES[i]] + row for i, row in enumerate(ADJ_MATRIX)])
                print(table)

            case ["matrix" | "mx", *action]:
                match action:
                    case ["help" | "h"]:
                        print_actions_help()

                    # Task 1
                    case ["find_neighbors" | "fn", v]:
                        v = int(v)
                        print(
                            f"Neigbors for vertex {VERTEX_NAMES[v]}:", ", ".join(matrix.find_neighbors(v, ADJ_MATRIX))
                        )

                    # Task 2
                    case ["check_chain" | "cc", *vs]:
                        vs = [int(v) for v in vs]
                        print("Chain!" if matrix.check_vertex_chain(vs, ADJ_MATRIX) else "Not a chain :(")

                    # Task 3
                    case ["find_vertexes" | "fv", value]:
                        value = int(value)
                        print(
                            "Edges: ",
                            ", ".join(str(v) for v in matrix.find_vertexes_with_greater_weight_sum(value, ADJ_MATRIX)),
                        )

                    # Task 4
                    case ["count" | "cnt"]:
                        print("Edges count:", matrix.get_edges_count(ADJ_MATRIX))

                    # Task 5
                    case ["size" | "s"]:
                        print(f"Size: {sys.getsizeof(ADJ_MATRIX)} bytes")

                    # Task 6
                    case ["test" | "t"]:
                        results = matrix.test_perfomace(ADJ_MATRIX)
                        print_results(results)

                    case unknown:
                        print(f"ERROR: Unknown action {unknown[0]!r} for command 'matrix'")
                        continue

            # Edges
            case ["edges" | "ed"]:
                print(*edges.get_edges_list(ADJ_MATRIX), sep="\n")

            case ["edges" | "ed", *action]:
                match action:
                    case ["help" | "h"]:
                        print_actions_help()

                    # Task 1
                    case ["find_neighbors" | "fn", v]:
                        v = int(v)
                        print(f"Neigbors for vertex {VERTEX_NAMES[v]}:", ", ".join(edges.find_neighbors(v, eds)))

                    # Task 2
                    case ["check_chain" | "cc", *vs]:
                        vs = [int(v) for v in vs]
                        print("Chain!" if edges.check_vertex_chain(vs, eds) else "Not a chain :(")

                    # Task 3
                    case ["find_vertexes" | "fv", value]:
                        value = int(value)
                        print(
                            "Edges: ",
                            ", ".join(str(v) for v in edges.find_vertexes_with_greater_weight_sum(value, eds)),
                        )

                    # Task 4
                    case ["count" | "cnt"]:
                        print("Edges count:", edges.get_edges_count(eds))

                    # Task 5
                    case ["size" | "s"]:
                        print(f"Size: {sys.getsizeof(eds)} bytes")

                    # Task 6
                    case ["test" | "t"]:
                        results = edges.test_perfomace(eds)
                        print_results(results)

                    case unknown:
                        print(f"ERROR: Unknown action {unknown[0]!r} for command 'edges'")
                        continue

            # Vertexes
            case ["vertexes" | "vs"]:
                print(*vertexes.get_vertex_list(ADJ_MATRIX), sep="\n")

            case ["vertexes" | "vs", *action]:
                match action:
                    case ["help" | "h"]:
                        print_actions_help()

                    # Task 1
                    case ["find_neighbors" | "fn", v]:
                        v = int(v)
                        print(
                            f"Neigbors for vertex {VERTEX_NAMES[v]}:",
                            ", ".join(vertexes.find_neighbors(v, vertex_list)),
                        )

                    # Task 2
                    case ["check_chain" | "cc", *vs]:
                        vs = [int(v) for v in vs]
                        print("Chain!" if vertexes.check_vertex_chain(vs, vertex_list) else "Not a chain :(")

                    # Task 3
                    case ["find_vertexes" | "fv", value]:
                        value = int(value)
                        print(
                            "Edges: ",
                            ", ".join(
                                str(v) for v in vertexes.find_vertexes_with_greater_weight_sum(value, vertex_list)
                            ),
                        )

                    # Task 4
                    case ["count" | "cnt"]:
                        print("Edges count:", vertexes.get_edges_count(vertex_list))

                    # Task 5
                    case ["size" | "s"]:
                        print(f"Size: {sys.getsizeof(vertex_list)} bytes")

                    # Task 6
                    case ["test" | "t"]:
                        results = vertexes.test_perfomace(vertex_list)
                        print_results(results)

                    case unknown:
                        print(f"ERROR: Unknown action {unknown[0]!r} for command 'vertexes'")
                        continue

            # Other
            case []:
                continue

            case unknown:
                print(f"ERROR: Unknown command {unknown[0]!r}")
                continue

        print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess exited with code 0")
