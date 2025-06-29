import heapq
def astar(graph,h,start,goal):
    openset = [(h[start],start,[start],0)]
    heapq.heapify(openset)
    visited = set()
    while openset:
        fscore, currentnode, path,gscore = heapq.heappop(openset)
        if currentnode == goal:
            return path,gscore
        if currentnode in visited:
            continue
        visited.add(currentnode)
        for neighbor, cost in graph[currentnode]:
            if neighbor not in visited:
                newgscore=gscore + cost
                newfscore=newgscore + h[neighbor]
                heapq.heappush(openset,(newfscore,neighbor,path + [neighbor], newgscore))
    return None, float('inf') 
graph = {
    'A':[('B',1), ('C',4)],
    'B':[('D',3), ('E',1)],
    'C':[('F',5)],
    'D':[],
    'E':[('F',2)],
    'D':[],
    'F':[]
}
h = {
    'A':7, 'B':6,'C':4,'D':2, 'E':1, 'F':0   
}
startnode='A'
goalnode='F'
path, cost = astar(graph,h,startnode,goalnode)
print("path:",path)
print("cost:",cost)