import itertools
import random
from collections import deque
from typing import Dict, List, Set


class User:
    def __init__(self, name: str) -> None:
        self.name = name


class SocialGraph:
    last_id: int
    users: Dict[int, User]
    friendships: Dict[int, Set[int]]

    def __init__(self) -> None:
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id: int, friend_id: int) -> None:
        """Creates a bi-directional friendship"""

        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name: str) -> None:
        """Create a new user with a sequential integer ID"""

        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users: int, avg_friendships: int) -> None:
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(num_users):
            self.add_user(str(i))

        friendships = random.choices(list(itertools.combinations(self.users, 2)), k=avg_friendships)

        for (first_user, second_user) in friendships:
            self.add_friendship(first_user, second_user)

    def get_all_social_paths(self, user_id: int) -> Dict[int, List[int]]:
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}

        container = deque()
        container.append([user_id])

        while container:
            path = container.popleft()

            user = path[-1]

            if user not in visited:
                visited[user] = path

                for friend in self.friendships[user]:
                    path_copy = path.copy()
                    path_copy.append(friend)
                    container.append(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 10)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
