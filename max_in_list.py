def maximum(arr):
    if not arr:
        return print('List is empty')
    if len(arr) == 1:
        return arr[0]
    else:
        max1 = arr.pop()
        max2 = maximum(arr)
        if max1 > max2:
            return max1
        else:
            return max2


print(maximum([2, 4, 1, 9, 5, 2, 6]))
print(maximum([]))
