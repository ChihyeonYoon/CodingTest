# from heapq import heapq,heappop, heappush
import heapq
def solution(N, road, K):
    answer = 0
    graph ={n+1:dict() for n in range(N)}
    
#     for start, end, weight in road:
#         if not graph.get(start):
#             graph[start]={}
#         if not graph.get(end):
#             graph[end]={}
            
#         if graph[start][end] >= weight:
#             graph[start][end]=weight 
            
#         if graph[end][start]>=weight :
#             graph[end][start]=weight 

    for edge in road:
        if edge[1] in graph[edge[0]]:
            if graph[edge[0]][edge[1]]>edge[2]:
                graph[edge[0]][edge[1]] = edge[2]
                graph[edge[1]][edge[0]] = edge[2]
        else:
            graph[edge[0]][edge[1]] = edge[2]
            graph[edge[1]][edge[0]] = edge[2]
        
    print(graph)
    # exit(0)
    
    def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
        distances[start] = 0  # 시작 값은 0이어야 함
        queue = []
        heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

        while queue:  # queue에 남아 있는 노드가 없으면 끝
            current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

            if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
                continue
    
            for new_destination, new_distance in graph[current_destination].items():
                distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
                if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                    distances[new_destination] = distance
                    heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
        return distances
    
    distances = dijkstra(graph,1)
    
    for v in distances.values():
        if v <= K:
            answer +=1
            

    return answer