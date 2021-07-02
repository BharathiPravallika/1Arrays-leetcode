#Find Numbers with Even Number of Digits
#"SOLUTION FOR LEETCODE"
class Solution:
  def findNumbers(self, nums: List[int]) -> int:
    counter = 0
    for num in nums:
      if (len(str(num)) % 2 == 0):
        counter += 1
    return counter
  
#"WHEN YOU WOULD LIKE TO TAKE INPUT FROM USER"
def findNumbers(nums):
        counter = 0
        for num in nums:
            if (len(str(num)) %2 == 0):
                counter += 1
        return counter
        
#nums = [5555,9001,4822,1771]
nums = [int(num) for num in input("").split()]
print(findNumbers(nums))

#"WHEN WE ARE TAKING DEFAULT INPUT"
def findNumbers(nums):
        counter = 0
        for num in nums:
            if (len(str(num)) %2 == 0):
                counter += 1
        return counter
        
nums = [5555,9001,4822,1771]
#nums = [int(num) for num in input("").split()]
print(findNumbers(nums))
