def merger_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    less_mid = merger_sort(arr[:mid])
    more_mid = merger_sort(arr[mid:])
    new_arr = []
    while True:
        if not more_mid:
            return new_arr + less_mid
        if not less_mid:
            return new_arr + more_mid
        if less_mid[0] < more_mid[0]:
            new_arr.append(less_mid.pop(0))
        else:
            new_arr.append(more_mid.pop(0))
