def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neigbhor in graph[node]:
            if neigbhor not in visited:
                visited.add(neigbhor)
                queue.append(neigbhor)
graph= {
    "0":["1","2"],
    "1":["2"],
    "2":["3","4"],
    "3":[],
    "4":[],
}     
start_node = "0"
print ("BFS traveseral from node",start_node)
bfs(graph, start_node)                 
