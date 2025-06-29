def dfs(graph, start , visited=None):
    if visited is None:
        visited = set()  
    visited.add(start)  
    print(start, end=' ')  
    for neighbor in graph [start]:  
        if neighbor not in visited:
           dfs(graph, neighbor, visited)
            
graph= {
    "5":["3","8"],
    "3":["2","4"],
    "8":["7"],
    "2":[],
    "4":[],
    "7":[],
    
}     
start_node = "5"
print ("dFS traveseral from node",start_node)
dfs(graph, start_node)  