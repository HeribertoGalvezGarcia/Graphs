import random
from ast import literal_eval
from collections import deque
from typing import List

from projects.adventure.player import Player
from projects.adventure.room import opposites
from projects.adventure.world import World

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = 'maps/test_line.txt'
# map_file = 'maps/test_cross.txt'
# map_file = 'maps/test_loop.txt'
# map_file = 'maps/test_loop_fork.txt'
map_file = 'maps/main_maze.txt'

# Loads the map into a dictionary
with open(map_file, 'r') as f:
    room_graph = literal_eval(f.read())

world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


def traverse_path() -> List[str]:
    player.current_room = world.starting_room
    movement_path = []
    q = deque()
    visited = set()

    while len(visited) < len(world.rooms):
        visited.add((current := player.current_room))

        if path := [d for d in current.get_exits() if current.get_room_in_direction(d) not in visited]:
            d = random.choice(path)
            q.append(d)
            player.travel(d)
            movement_path.append(d)
        else:
            d = q.pop()
            player.travel(opposites[d])
            movement_path.append(opposites[d])

    return movement_path


while len(traversal_path := traverse_path()) > 950:
    continue

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description()
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
