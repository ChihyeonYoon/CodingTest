def solution(wallpaper):
    answer = []
    points_x = []
    points_y =[]
    for i,line in enumerate(wallpaper):
        for j,point in enumerate(line):
            if point == '#':
                points_y.append(i)
                points_x.append(j)

    answer.append(min(points_y))
    answer.append(min(points_x))
    answer.append(max(points_y)+1)
    answer.append(max(points_x)+1)
    
    return answer