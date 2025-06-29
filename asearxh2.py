import heapq

def astar(graph, start, goal):
    open_set = [(0, start, 0)]  
    closed_set = set()

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    parents = {}
    while open_set:
        current_f, current_node, current_cost = heapq.heappop(open_set)

        if current_node == goal:
            path = [current_node]
            while current_node in parents:
                current_node = parents[current_node]
                path.append(current_node)
            return path[::-1], current_cost 

        closed_set.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current_node] + cost

            if tentative_g_score < g_score[neighbor]:
                parents[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                if (f_score[neighbor], neighbor) not in open_set:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor, current_cost + cost)) 

    return None, -1 

graph = {
    'S': {'A': 5, 'B': 4},
    'A': {'S': 5, 'G': 0},
    'G': {'A': 1, 'C': 2},
    'C': {'B': 4, 'G': 0},
    'B': {'S': 5, 'C': 2}
  
}

def heuristic(node1, node2):
  
    return abs(ord(node1) - ord(node2))

start_node = 'S'
goal_node = 'G'

path, cost = astar(graph, start_node, goal_node) 

if path:
    print(f"Shortest path from {start_node} to {goal_node}: {path}")
    print(f"Cost of the path: {cost}")
else:
    print(f"No path found from {start_node} to {goal_node}")
    print(f"No path found from {start_node} to {goal_node}")