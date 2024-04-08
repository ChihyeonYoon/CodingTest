from heapq import heappush, heappop, heapify
def solution(operations):
    answer = []
    
    min_heap = []
    max_heap = []
    
    for operation in operations:
        ins, v = operation.split(" ")[0], int(operation.split(" ")[1])
        if ins == 'I':
            heappush(min_heap, v)
            heappush(max_heap, (-1)*v)

        if ins == 'D' and min_heap and max_heap:
            if v == 1: # heappop max
                v_ = heappop(max_heap)
                min_heap.remove((-1)*v_) #remove v_
                heapify(min_heap)
                
            
            if v == -1: # heappop min
                v_ = heappop(min_heap)
                max_heap.remove((-1)*v_) #remove v_
                heapify(max_heap)

    print(min_heap)
    print(max_heap)
    return [(-1)*max_heap[0], min_heap[0]] if min_heap and max_heap else [0,0]