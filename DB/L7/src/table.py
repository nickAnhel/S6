import typing as tp

import prettytable


def print_table(
    columns: list[str],
    data: tp.Sequence,
) -> None:
    table = prettytable.PrettyTable(columns)
    table.add_rows(data)
    print(table)
