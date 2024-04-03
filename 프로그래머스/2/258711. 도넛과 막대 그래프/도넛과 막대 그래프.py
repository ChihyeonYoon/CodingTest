def solution(edges):
    answer = [0,0,0,0] # 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수
    nodeCnt = {}
    for edge in edges:
        node1, node2 = edge # out_node, in_node
        if not nodeCnt.get(node1):
            nodeCnt[node1] = [0,0]
        if not nodeCnt.get(node2):
            nodeCnt[node2] = [0,0]
        nodeCnt[node1][0] +=1
        nodeCnt[node2][1] +=1 # {node:[out_edge, in_edge]}

    # print(nodeCnt)

    for node, edge in nodeCnt.items():
        out_edge, in_edge = edge

        if out_edge >=2 and in_edge == 0: # 생성 노드
            answer[0] = node
        elif out_edge ==0 and in_edge >=1: # 막대그래프의 노드
            answer[2] +=1
        elif out_edge >=2 and in_edge >=2: # 8자 그래프의 노드
            answer[3] +=1
        
    gen_node = answer[0]
    answer[1] = nodeCnt[gen_node][0] - answer[2] - answer[3] # gen_node의 out_edge 수 에서 막대그래프 수, 8자그래프 수 를 뺀다

    return answer