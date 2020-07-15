from typing import Tuple, List


def earliest_ancestor(ancestors: List[Tuple[int, int]], starting_node: int) -> int:
    def recur(point: int) -> List[int]:
        if not (paths := [i for i, j in ancestors if point == j]):
            return [point]

        return max(([starting_node, *recur(path)] for path in paths), key=len)

    return points[-1] if len((points := recur(starting_node))) > 1 else -1
