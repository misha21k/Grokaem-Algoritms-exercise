def binary_search(arr, search):
    mid = len(arr)//2
    guess = arr[mid]
    if search == guess:
        return mid
    elif search > guess:
        return mid + 1 + binary_search(arr[mid + 1:], search)
    else:
        return binary_search(arr[:mid], search)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(binary_search(arr, 20))