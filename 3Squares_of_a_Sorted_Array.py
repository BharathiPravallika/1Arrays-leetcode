#Squares of a sorted array ----> TAKING INPUT FROM USER SOLUTION
def squareofarr(nums):
    res = []
    for num in nums:
        res.append(num ** 2)
    return sorted(res)
#nums = [1, 2, 3, 4, 5, 6, 7]
#ts = int(input("enter number of test cases"))
nums = [int(num) for num in input("").split()]
print(squareofarr(nums))





#Squares of a sorted array ----> TAKING DEFAULT INPUT BY OURSELVES
def squareofarr(nums):
    res = []
    for num in nums:
        res.append(num ** 2)
    return sorted(res)
nums = [1, 2, 3, 4, 5, 6, 7]
#ts = int(input("enter number of test cases"))
#nums = [int(num) for num in input("").split()]
print(squareofarr(nums))




#Squares of a sorted array ----> LEETCODE SOLUTION
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
          res.append(num ** 2)
        return sorted(res)
      
      
