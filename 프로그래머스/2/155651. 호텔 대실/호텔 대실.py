def solution(book_time):
    answer = 0
    new_book_time = []
    for start, end in book_time:
        new_book_time.append([int(start.split(':')[0]) * 60 + int(start.split(':')[1]),
                             int(end.split(':')[0]) * 60 + int(end.split(':')[1])])
    new_book_time.sort(key=lambda x:x[0])
    # print(new_book_time)
    
    hotel = [[] for _ in range(len(new_book_time))]
    
    
    for start, end in new_book_time:
        
        for room in hotel:
            if not room:
                room.append([start,end])
                break
            if room and room[-1][-1] + 10 <= start:
                room.append([start,end])
                break
            if room and room[-1][-1] + 10 > start:
                continue
    # print(hotel)
    answer = len(hotel)- hotel.count([])
    return answer