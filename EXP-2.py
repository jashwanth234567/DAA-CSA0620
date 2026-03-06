def function(nums1, nums2, n, m):
    result = []
    c = 0
    cc = 0

    for i in range(n):
        for j in range(m):
            if nums1[i] == nums2[j]:
                c += 1
                break

    result.append(c)

    for i in range(m):
        for j in range(n):
            if nums2[i] == nums1[j]:
                cc += 1
                break

    result.append(cc)

    return result


nums1 = [2,3,2]
print("nums1:-", nums1)

nums2 = [1,2]
print("nums2:-", nums2)

n = len(nums1)
m = len(nums2)

print("result:-", function(nums1, nums2, n, m))
