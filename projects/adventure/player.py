from projects.adventure.room import Room


class Player:
    def __init__(self, starting_room: Room) -> None:
        self.current_room = starting_room

    def travel(self, direction: str, show_rooms: bool = False) -> None:
        if (next_room := self.current_room.get_room_in_direction(direction)) is None:
            raise ValueError('You cannot move in that direction.')

        self.current_room = next_room

        if show_rooms:
            next_room.print_room_description()

