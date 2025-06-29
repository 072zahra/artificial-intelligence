class GraphNode:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic

class BestFirstSearchAlgorithm:
    def __init__(self, adjacency_list, heuristics):
        self.adjacency_list = adjacency_list
        self.heuristics = heuristics

    def execute_search(self, start, goal):
        open_list = []
        closed_set = set()

        start_node = GraphNode(start, self.heuristics[start])
        open_list.append(start_node)

        while open_list:
            open_list.sort(key=lambda node: node.heuristic)
            current_node = open_list.pop(0)

            if current_node.name == goal:
                print(f"Goal '{goal}' found!")
                return True

            if current_node.name in closed_set:
                continue

            closed_set.add(current_node.name)
            print(f"Exploring node: {current_node.name} with heuristic value: {current_node.heuristic}")

            for neighbor, cost in self.adjacency_list.get(current_node.name, []):
                if neighbor not in closed_set:
                    neighbor_node = GraphNode(neighbor, self.heuristics[neighbor])
                    open_list.append(neighbor_node)

        print(f"Goal '{goal}' not found.")
        return False

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 3)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 6)],
    'F': [('G', 1)],
    'G': []
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 12,
    'E': 4,
    'F': 1,
    'G': 0
}

start_node = 'B'
goal_node = 'F'

bfs_algorithm = BestFirstSearchAlgorithm(graph, heuristics)
bfs_algorithm.execute_search(start_node, goal_node)
