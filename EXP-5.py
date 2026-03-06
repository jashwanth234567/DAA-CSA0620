def find_max(arr):
    if not arr:
        return None

    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


arr = [1,2,3,4,5]
print(find_max(arr))
