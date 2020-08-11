from queue import Queue
from stack import Stack
# lets do a graph adjacency list


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

        else:
            raise IndexError("Vertex does not exist!")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # Create an empty queue and enqueue starting_vertex
        q = Queue()
        q.enqueue(starting_vertex_id)

        # Create a set to store the visited vertices
        visited = set()

        # While the queue is not empty
        while q.size > 0:
            # dequeue the first vertex
            v = q.dequeue()

            # if vertex has not been visited
            if v not in visited:
                # mark the vertex as visited
                visited.add(v)
                # print it for debug
                print(v)

                # add all of its neighbors to the back of the queue
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex_id):
        # Create an empty stack and push starting_vertex
        s = Stack()
        s.push(starting_vertex_id)

        # Create a set to store the visited vertices
        visited = set()

        # While the stack is not empty
        while s.size > 0:
            # pop the last vertex
            v = s.pop()

            # if vertex has not been visited
            if v not in visited:
                # mark the vertex as visited
                visited.add(v)
                # print it for debug
                print(v)

                # add all of its neighbors to the top of the stack
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)

    def bfs(self, starting_vertex_id, target_vertex_id):
        # create an empty queue and enqueue PATH to the starting_vertex_id

        q = Queue()

        q.enqueue([starting_vertex_id])

        # create a set to store the visited vertices

        visited = set()

        # while the queue is not empty:
        while q.size() > 0:
            # dequeue the first PATH
            path = q.dequeue()
            # grab the last vertex from the PATH
            last_vertex = path[-1]

            # check if the vertex has not been visited
            if last_vertex not in visited:
                # is it the target_vertex??
                if last_vertex == target_vertex_id:
                    # return the PATH
                    return path
                # mark the node as visited
                visited.add(last_vertex)

            # then add a PATH to neighbors to the back of the queue

            neighbors = self.get_neighbors(last_vertex)

            for neighbor in neighbors:
                # make a copy of the PATH
                new_path = list(path)

                # append the neighbor to the back of the PATH
                new_path.append(neighbor)
                # enqueue our new PATH
                q.enqueue(new_path)

        # return None
        return None

    def dfs(self, starting_vertex_id, target_vertex_id):

        s = Stack()

        visited = set()

        s.push([starting_vertex_id])

        while s.size() > 0:

            path = s.pop()

            last_vertex = path[-1]

            if last_vertex not in visited:

                if last_vertex == target_vertex_id:
                    return path

                visited.add(path)

            neighbors = self.vertices[last_vertex]

            for neighbor in neighbors:
                new_path = [path]

                new_path.append(neighbor)

                s.push(new_path)

        return None
