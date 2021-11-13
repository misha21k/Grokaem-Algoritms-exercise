def bubble_sort(arr):
    length = len(arr)
    for i in range(1, length):
        f = True
        for j in range(0, length-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = (arr[j+1], arr[j])
                f = False
        if f:
            break
    return arr
