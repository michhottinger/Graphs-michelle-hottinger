from room import Room
from player import Player
from world import World
from collections import deque
from queue import queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def return_adjacent(direction):
    if direction == "n":
        return "e"
    if direction == "s":
        return "w"
    if direction == "e":
        return "s"
    if direction == "w":
        return "n"

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# Outline of code:
# players current room is start
# travel(direction)
# log direction in traversal
# loop through this
# if dead end (no-unexplored paths)
# BFS to nearest room that contains exit with "?"
# Add the room to queue and add direction to traversal path
# for d in directions:
#     traversal_path.append(d)

    
traversal_path = []
steps = 0
visited = {}
def traversal(current_room):
    q = queue()
   
    visited.add(room.id)
    visits = 1
    q.put(0, room, traversal_path, steps, visited, visits())
    
    while not q.empty():
        room, traversal_path, steps, visited, visits() = q.get()
        if len(visited) == room_count:
            return path
        for direction in room.get_exits():
            next_room = room.get_room_in_direction(direction)
            
            next_path = next_path.append(direction)
            
            next_steps = steps + 1
            
            next_visited = visited
            next_visits = visits
            
            if next_room.id not in next_visited:
                next_visited.add(next_room.id)
                next_visits = visits + 1
                
            q.put(next_room, next_path, next_steps, next_visited, next_visits())

    return traversal_path


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
"""
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
"""