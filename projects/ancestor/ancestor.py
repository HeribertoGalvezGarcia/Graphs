from typing import List, Tuple


def earliest_ancestor(ancestors: List[Tuple[int, int]], starting_node: int) -> int:
    graph = {}

    for (parent, child) in ancestors:
        try:
            graph[child].add(parent)
        except KeyError:
            graph[child] = {parent}

    def recur(point: int) -> List[int]:
        if (paths := graph.get(point)) is None:
            return [point]

        return max(([starting_node, *recur(path)] for path in paths), key=lambda x: (len(x), -x[-1]))

    return points[-1] if len((points := recur(starting_node))) > 1 else -1
