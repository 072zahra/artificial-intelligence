def dfs(graph, start, end, path):
    path = path + [start]
   
    if start == end:
        return path
    
    if start in graph:
        for neighbor in graph[start]:
            if neighbor not in path:
                result = dfs(graph, neighbor, end, path)
                if result:
                    return result
    
    return None

def find_path(graph, start, end):
    if start not in graph or end not in graph:
        return "No path found."

    path = dfs(graph, start, end, [])
    if path:
        return "Path found"
    else:
        return "No path found."

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C', 'I'],
    'H': ['E'],
    'I': ['G']
}

start_node = 'A'
end_node = 'l'
print(find_path(graph, start_node, end_node))