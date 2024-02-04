import heapq

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def astar(maze, start, end):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(node):
        neighbors = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent and diagonal neighbors
            node_position = (node.position[0] + new_position[0], node.position[1] + new_position[1])
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue
            if maze[node_position[0]][node_position[1]] == 1:
                continue
            new_node = Node(node, node_position)
            neighbors.append(new_node)
        return neighbors

    open_list = []
    closed_list = []

    start_node = Node(None, start)
    end_node = Node(None, end)

    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        neighbors = get_neighbors(current_node)
        for neighbor in neighbors:
            if neighbor in closed_list:
                continue
            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, end_node.position)
            neighbor.f = neighbor.g + neighbor.h

            if any(open_node == neighbor and open_node.f < neighbor.f for open_node in open_list):
                continue

            heapq.heappush(open_list, neighbor)

    return None

# Example maze with obstacles
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

start = (0, 0)
end = (7, 7)
path = astar(maze, start, end)
if path:
    print("Path found:", path)
else:
    print("No path found")
