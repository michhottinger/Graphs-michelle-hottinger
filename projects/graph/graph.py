"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()#holds edges
        
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)#there's an edge from v1 to v2
        else:
            raise IndexError("nonexistent vert")
            
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #create an empty queue
        q = Queue()
        #create a set to store teh visited nodes
        visited = set()
        #init: enqueue the starting node
        q.enqueue(starting_vertex)
        #while the queue isn't empty
        while q.size() > 0:
            #dequeue the first item
            v = q.dequeue()
            #if v has not been visited:
            if v not in visited:
                #add it to the visited set
                visited.add(v)
                print(f'Visited {v}')
                
                #add all nieghbors to the queue:
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()

        # Create a set to store the visited nodes
        visited = set()

        # Init: push the starting node
        s.push(starting_vertex)

        # While the stack isn't empty
        while s.size() > 0:
            # pop the first item
            v = s.pop()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)

                # Do something with the node
                print(f"Visited {v}")

                # Add all neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited = []):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
#pseudocode from TK notes
#         DFS_visit(v):
#     v.color = gray

#     for neighbor of v.adjacent_nodes:
#         if neighbor.color == white:
#             neighbor.parent = v
#             DFS_visit(neighbor)

    #v.color = black
    
#using a list and not a dict here, so runtime is linear rather than constant
#list returns all verts
        
        
        visited +=[starting_vertex]
        
        # Recur for all the vertices  
        # adjacent to this vertex 
        for neighbor in self.get_neighbors(starting_vertex): 
            if neighbor not in visited: 
                visited = self.dft_recursive(neighbor, visited)
                
        return visited
        
        

    def bfs(self, starting_vertex, destination_vertex, path=[]):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        # keep track of explored nodes
        explored = []
        #keep track of all the paths to be checked
        queue = [[starting_vertex]]
        #return the path if start is the goal
        if starting_vertex == destination_vertex:
            return ("start = finish")
        
        while queue:
            #pop first path from queue
            path = queue.pop(0)
            #get the last node from path
            node = path[-1]
            if node not in explored:
                #got through all neighbor nodes and add to new_path
                for neighbor in self.get_neighbors(node):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    if neighbor == destination_vertex:
                        return new_path
                    
                explored.append(node)
                
        return "Sorry no path"
                
                
            
        
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], result=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path += [starting_vertex]
        if starting_vertex == destination_vertex:
            result.append(path)
            
        else:
            for neighbor in self.get_neighbors(starting_vertex):
                if neighbor not in path:
                    self.dfs_recursive(neighbor, destination_vertex, 
                                              path[:], result) 
            
        return result


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
