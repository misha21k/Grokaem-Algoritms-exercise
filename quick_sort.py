def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pilot = array[0]
        less = [i for i in array[1:] if i <= pilot]
        greater = [i for i in array[1:] if i > pilot]
        return quick_sort(less) + [pilot] + quick_sort(greater)
