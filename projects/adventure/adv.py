from room import Room
from player import Player
from world import World
from collections import deque


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


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited = {}

# Outline of code:
# players current room is start
# travel(direction)
# log direction somewhere
# loop through this
# if dead end (no-unexplored paths)
# BFS to nearest room that contains exit with "?"
# Add the room to queue and add direction to traversal path
# for d in directions:
#     traversal_path.append(d)
# def Traversal(current_room):
#     current_room = player.current_room.id
#     exits = player.current_room.get_exits
#     prev_room = None#to start there is no previous
#     s = Stack()
        

def opp_dir(direction):
    if direction == "n":
        return "s"
    if direction == "s":
        return "n"
    if direction == "e":
        return "w"
    if direction == "w":
        return "e"


#we will need the direction to be appended to the traversal path for each move!
def move(direction):
        player.travel(direction)#sets current room to next room
        traversal_path.append(direction)

#We will need to add the room ID and all the exits to the visited dict to keep track of where we have been and where we can go next
def add_to_visited(current_room_id, exits):
    visited[current_room_id] = {}
    for e in exits:
        visited[current_room_id][e] = None

#lets start to traverse this graph
def dft_traversal(current_room):
    current_room = player.current_room.id
    current_exits = player.current_room.get_exits()
    
    prev_room = None#starts at None
    s = Stack()
#    direction[0], current_room[1], prev[2], exits[3] indexes of list
    s.push([None, current_room, prev_room, current_exits])
    while len(visited) < 499:
        curr_node = s.pop()
        direction = curr_node[0]
        current_room = curr_node[1]
        prev_room = curr_node[2]
        curr_exits = curr_node[3]
        if current_room not in visited:
            add_to_visited(current_room, curr_exits)#this adds the room id and exits to visited list
        if direction is not None:
            visited[current_room][opp_dir(direction)] = prev_room#set up the previous node
        
        if prev_room is not None:
            visited[prev_room][direction] = current_room#set up the current node
            
        for d in visited[current_room].keys():#find all the directions you can go

            if visited[current_room][d] is None:
                s.push(curr_node)
                prev = player.current_room.id #We are going to move direction forward for curr
                move(d)#move will add just the directions to traverse_path
                s.push([d, player.current_room.id, prev, player.current_room.get_exits()])
                #add direction, room id, prev and exits to the stack
                break
        if current_room == player.current_room.id:
            move(opp_dir(direction))#moves current room to next room in opp direction


dft_traversal(player.current_room.id)

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