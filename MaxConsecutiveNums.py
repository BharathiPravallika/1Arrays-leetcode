#This is for default input from our side

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


#This is for user input
def consecutiveones(arr, n):
    counter = 0
    maxm = 0
    for i, n in enumerate(arr):
        if arr[i] == 1:
            counter += 1
            maxm = max(maxm, counter)
        else:
            counter = 0
    return maxm

#arr = [0, 1, 1, 0, 0, 1, 1, 1, 1, 1]
arr = [int(i) for i in input("").split()]
n = len(arr)
print(consecutiveones(arr, n))


#Now leetcode solution:
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxm = 0
        for i, n in enumerate(nums):
            if nums[i] == 1:
                count += 1
                maxm = max(count, maxm)
            else:
                count = 0
        return maxm
        
