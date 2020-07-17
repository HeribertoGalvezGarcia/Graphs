from typing import Dict, List, Optional, Tuple

from projects.adventure.room import Room


class World:
    starting_room: Optional[Room]
    rooms: Dict[int, Room]
    room_grid: List[List[Optional[Room]]]
    grid_size: int

    def __init__(self) -> None:
        self.starting_room = None
        self.rooms = {}
        self.room_grid = []
        self.grid_size = 0

    def load_graph(self, room_graph: Dict[int, Tuple[Tuple[int, int], Dict[str, int]]]):
        grid_size = 1

        for id_, ((x, y), _) in room_graph.items():
            grid_size = max(grid_size, x, y)
            self.rooms[id_] = Room(f'Room {id_}', f'({x}, {y})', id_, x, y)

        self.room_grid = []
        grid_size += 1
        self.grid_size = grid_size

        self.room_grid = [[None] * grid_size for _ in range(grid_size)]

        for id_, ((x, y), directions) in room_graph.items():
            room = self.rooms[id_]
            self.room_grid[self.grid_size - y - 1][x] = room

            for direction, connecting_room in directions.items():
                room.connect_rooms(direction, self.rooms[connecting_room])

        self.starting_room = self.rooms[0]

    def print_rooms(self):
        fmt = f'#{"#####" * self.grid_size}#'
        for row in self.room_grid:
            if not any(row):
                continue

            # PRINT NORTH CONNECTION ROW
            fmt += '\n#'
            for room in row:
                fmt += '  |  ' if room is not None and room.n_to is not None else '     '

            fmt += '#\n'

            # PRINT ROOM ROW
            fmt += '#'
            for room in row:
                fmt += '-' if room is not None and room.w_to is not None else ' '
                fmt += f'{room.id:0>3}' if room is not None else '   '
                fmt += '-' if room is not None and room.e_to is not None else ' '

            fmt += '#\n'

            # PRINT SOUTH CONNECTION ROW
            fmt += '#'
            for room in row:
                fmt += '  |  ' if room is not None and room.s_to is not None else '     '

            fmt += '#'

        fmt += f'\n#{"#####" * self.grid_size}#'

        print(fmt)
