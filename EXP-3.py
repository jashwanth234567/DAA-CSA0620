def sumCounts(nums):
    n = len(nums)
    total = 0

    for i in range(n):
        s = set()
        for j in range(i, n):
            s.add(nums[j])
            total += len(s) ** 2

    return total


nums = [1, 2, 1]
print(sumCounts(nums))
