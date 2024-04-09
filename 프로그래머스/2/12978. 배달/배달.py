import heapq
def solution(N, road, K):
    answer = 0
    graph = {}
    for start, end, weight in road:
        if not graph.get(start):
            graph[start] = {}
        if not graph.get(end):
            graph[end] = {}

        if not graph[start].get(end):
            graph[start][end] = float('inf')
        if graph[start][end] > weight:
            graph[start][end] = weight
        
        if not graph[end].get(start):
            graph[end][start] = float('inf')
        if graph[end][start] > weight:
            graph[end][start] = weight
    # print(graph)
    '''
    {start:{end:weight}}
    
    {
        1: {2: 1, 
            4: 2}, 
        2: {1: 1, 
            3: 3, 
            5: 2}, 
        3: {2: 3, 
            5: 1}, 
        4: {1: 2, 
            5: 2},
        5: {2: 2, 
            3: 1, 
            4: 2},
    } 
    '''

    from collections import deque
    def bfs(graph, start):
        
        q = deque([(start,0)]) # (node, depth)
        visited = {start:0} # {node:depth}

        while q:
            cur_node, cur_depth = q.popleft()
    
            for next_node in graph[cur_node]:
                if next_node not in visited:
                    next_depth = cur_depth + 1
                    visited[next_node] = next_depth
                    q.append((next_node, next_depth))

        return visited

    
    
    
    import heapq
    def dijkstra(graph, start):
        pq=[]
        heapq.heappush(pq, (0,start)) # (weight, node)
        visited={} # {node:cost}

        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            
            if cur_node not in visited:
                visited[cur_node] = cur_cost
                for next_node in graph[cur_node]:
                    next_cost = cur_cost + graph[cur_node][next_node]
                    heapq.heappush(pq, (next_cost, next_node))
                    
        return visited
    
    visited = dijkstra(graph,1)
    print(visited)
    for cost in visited.values():
        if cost <= K:
            answer +=1

    # visited = bfs(graph,1)
    # print(visited)
    
    return answer