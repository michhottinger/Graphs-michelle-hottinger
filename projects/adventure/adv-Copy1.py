from room import Room
from player import Player
from world import World
from collections import deque
import threading, queue

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

visited = {}

def move(direction):
    player.travel(direction)
    traversal_path.append(direction)

def recurse(direction):
    traversal(direction)
    move(direction)
    
def traversal(previous=0):
    
    current_room = player.current_room.id
   
    for key in visited:
        if key == current_room:
            #print("been here:", current_room)
            return
    visited[current_room] = {}
    #print('adding:', current_room)
    
    exits = player.current_room.get_exits()
    for dir in exits:
        if dir == 'n' and previous is not dir:
            move('n')
            recurse('s')
        elif dir == 's' and previous is not dir:
            move('s')
            recurse('n')
        elif dir == 'e' and previous is not dir:
            move('e')
            recurse('w')
        elif dir == 'w' and previous is not dir:
            move('w')
            recurse('e')
#     move = player.current_room.connect_rooms(direction, connecting_room)
#     for path in move:
#         if move == 'n' and previous is not move:
#             player.travel('n')
#             traversal_path.append('n')
#             traversal('s')
#             player.travel('s')
#             traversal_path.append('s')
traversal()
                                 

    
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