import numpy as np


PROFIT_FUNCTIONS = {
    1: [0.0, 0.3, 0.4, 0.6, 0.5, 0.7, 0.8, 0.9],
    2: [0.0, 1.0, 1.1, 1.2, 1.2, 1.4, 1.5, 1.7],
    3: [0.0, 1.3, 1.4, 1.6, 1.6, 1.5, 1.8, 1.7],
    4: [0.0, 0.9, 0.9, 1.0, 1.1, 1.1, 1.4, 1.4],
    5: [0.0, 1.0, 1.3, 1.5, 1.7, 1.9, 2.1, 2.3],
}

TOTAL_RESOURCE = 7
ENTERPRISES = 5


def solution(
    enterprises: int,
    total_resource: int,
    profit_functions: dict[int, list[float]],
) -> list[int]:
    dp = np.zeros((enterprises + 2, total_resource + 1))
    decision = np.zeros((enterprises + 1, total_resource + 1), dtype=int)

    for i in range(enterprises, 0, -1):
        for s in range(total_resource + 1):
            best_profit = -np.inf

            for x in range(s + 1):
                current_profit = profit_functions[i][x] + dp[i + 1][s - x]

                if current_profit > best_profit:
                    best_profit = current_profit
                    decision[i][s] = x

            dp[i][s] = best_profit

    resource_left = total_resource
    allocation = []
    for i in range(1, enterprises + 1):
        x = decision[i][resource_left]
        allocation.append(x)
        resource_left -= x

    return allocation


def print_solution(
    allocation: list[int],
    profit_functions: dict[int, list[float]],
) -> None:
    print("Optimal Resource Allocation and Profit Calculation:")
    print("-" * 50)

    total_profit = 0.0
    for i, x in enumerate(allocation, start=1):
        profit = profit_functions[i][x]
        total_profit += profit
        print(f"Enterprise {i}: allocate {x} unit(s) → profit = {profit:.1f}")

    print("-" * 50)
    print(f"\nTotal profit: {total_profit:.1f}")


def main() -> None:
    allocation = solution(ENTERPRISES, TOTAL_RESOURCE, PROFIT_FUNCTIONS)
    print_solution(allocation, PROFIT_FUNCTIONS)


if __name__ == "__main__":
    main()
