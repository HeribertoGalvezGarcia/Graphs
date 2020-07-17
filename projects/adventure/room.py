from __future__ import annotations

from typing import Dict, List, Optional

opposites = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e',
}


class Room:
    directions: Dict[str, Optional[Room]]

    def __init__(self, name: str, description: str, id_: int, x: int, y: int) -> None:
        self.id = id_
        self.name = name
        self.description = description
        self.x = x
        self.y = y

        self.directions = {
            'n': None,
            's': None,
            'e': None,
            'w': None
        }

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f'\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.get_exits_string()}\n'

    @property
    def n_to(self) -> Optional[Room]:
        return self.get_room_in_direction('n')

    @property
    def s_to(self) -> Optional[Room]:
        return self.get_room_in_direction('s')

    @property
    def e_to(self) -> Optional[Room]:
        return self.get_room_in_direction('e')

    @property
    def w_to(self) -> Optional[Room]:
        return self.get_room_in_direction('w')

    def print_room_description(self) -> None:
        print(str(self))

    def get_exits(self) -> List[str]:
        return [direction for direction, value in self.directions.items() if value is not None]

    def get_exits_string(self) -> str:
        return f'Exits: {self.get_exits()}'

    def connect_rooms(self, direction: str, connecting_room: Room) -> None:
        try:
            opposite = opposites[direction]
        except KeyError:
            raise ValueError('INVALID ROOM CONNECTION')
        else:
            self.directions[direction] = connecting_room
            connecting_room.directions[opposite] = self

    def get_room_in_direction(self, direction: str) -> Optional[Room]:
        return self.directions.get(direction)
