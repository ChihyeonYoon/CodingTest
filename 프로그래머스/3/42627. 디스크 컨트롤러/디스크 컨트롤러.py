from heapq import heapify, heappop, heappush
def solution(jobs):
    jobs.sort(key=lambda x: x[0])  # 요청 시점 기준으로 정렬
    time, total_time, len_ = 0, 0, len(jobs)
    heap = []  # 최소 힙 (소요 시간 기준)

    while jobs or heap:
        # 현재 시점에서 처리 가능한 작업들을 heap에 추가
        while jobs and jobs[0][0] <= time:
            request_time, processing_time = jobs.pop(0)
            heappush(heap, (processing_time, request_time))

        if heap:
            # heap에서 소요 시간이 가장 짧은 작업 선택
            processing_time, request_time = heappop(heap)
            time += processing_time
            total_time += time - request_time
        else:
            # 현재 시점에서 처리 가능한 작업이 없으면 시간을 1 증가
            time += 1

    return total_time // len_