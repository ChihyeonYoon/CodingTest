def solution(array):
    answer = 0
    
    arr = [0 for i in range(max(array)+1)]
    # print(arr)

    for n in array:
        arr[n]+=1

    # print(arr)
    # print(arr.count(1))

    if arr.count(max(arr))>1:
        return -1
    else:
        return arr.index(max(arr))