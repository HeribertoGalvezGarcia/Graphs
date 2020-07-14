"""
Simple graph implementation
"""
from typing import Dict, Generic, Hashable, List, Optional, Set, TypeVar

from util import Queue, Stack  # These may come in handy

T = TypeVar('T', bound=Hashable)


class Graph(Generic[T]):
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self) -> None:
        self.vertices: Dict[T, Set[T]] = {}

    def add_vertex(self, vertex_id: T) -> None:
        """
        Add a vertex to the graph.
        """

        self.vertices[vertex_id] = set()

    def add_edge(self, v1: T, v2: T) -> None:
        """
        Add a directed edge to the graph.
        """

        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id: T) -> Set[T]:
        """
        Get all neighbors (edges) of a vertex.
        """

        return self.vertices[vertex_id]

    def traverse(self, starting_vertex: T, breadth: bool) -> None:
        container = Queue() if breadth else Stack()
        add = container.enqueue if breadth else container.push
        remove = container.dequeue if breadth else container.pop

        visited = set()

        add(starting_vertex)

        while container.size() > 0:
            value = remove()

            if value not in visited:
                visited.add(value)

                print(value)

                for vertex in self.get_neighbors(value):
                    add(vertex)

    def bft(self, starting_vertex: T) -> None:
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        self.traverse(starting_vertex, True)

    def dft(self, starting_vertex: T) -> None:
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        self.traverse(starting_vertex, False)

    def dft_recursive(self, starting_vertex: T, visited: Set[T] = None) -> None:
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        visited = visited if visited is not None else set()

        if starting_vertex in visited:
            return

        visited.add(starting_vertex)
        print(starting_vertex)

        for vertex in self.get_neighbors(starting_vertex):
            self.dft_recursive(vertex, visited)

    def search(self, starting_vertex: T, destination_vertex: T, breadth: bool) -> List[T]:
        container = Queue() if breadth else Stack()
        add = container.enqueue if breadth else container.push
        remove = container.dequeue if breadth else container.pop

        visited = set()

        add([starting_vertex])

        while container.size() > 0:
            path = remove()

            value = path[-1]

            if value not in visited:
                if value == destination_vertex:
                    return path

                visited.add(value)

                for vertex in self.get_neighbors(value):
                    path_copy = path.copy()
                    path_copy.append(vertex)
                    add(path_copy)

    def bfs(self, starting_vertex: T, destination_vertex: T) -> List[T]:
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        return self.search(starting_vertex, destination_vertex, True)

    def dfs(self, starting_vertex: T, destination_vertex: T) -> List[T]:
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        return self.search(starting_vertex, destination_vertex, False)

    def dfs_recursive(self, starting_vertex: T, destination_vertex: T, visited: Set[T] = None) -> Optional[List[T]]:
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        if destination_vertex == starting_vertex:
            return [destination_vertex]

        visited = visited if visited is not None else set()

        if starting_vertex in visited:
            return

        visited.add(starting_vertex)

        for vertex in self.get_neighbors(starting_vertex):
            if (path := self.dfs_recursive(vertex, destination_vertex, visited)) is not None:
                return [starting_vertex, *path]


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
