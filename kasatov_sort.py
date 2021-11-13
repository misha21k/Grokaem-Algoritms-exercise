def kasatov_sort(arr):
    i = 1
    length = len(arr)
    while i < length:
        if arr[i] >= arr[i-1]:
            i += 1
        else:
            arr[i], arr[i-1] = (arr[i-1], arr[i])
            if i > 1:
                i -= 1
    return arr
