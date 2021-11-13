def sum(arr):
    if arr:
        return arr.pop(0) + sum(arr)
    else:
        return 0


print(sum([2, 3, 4]))
print(sum([]))
