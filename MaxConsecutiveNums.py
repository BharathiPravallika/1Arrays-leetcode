def consecutiveones (arr, nums):
    count = 0
    maxm = 0
    for i in range(0,nums):
        if arr[i] == 1:
            count += 1
            maxm = max(count, maxm)
        else:
            count = 0
    return maxm
arr = [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
nums = len(arr)
print(consecutiveones (arr, nums))
