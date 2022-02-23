# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


# My solution: Two Sum problem number 1. 

class Solution:
    def twoSum(nums, target):
        working_dictionary = {}
        for i, n in enumerate(nums):
            if target - n in working_dictionary and working_dictionary[target - n] != i:
                return [working_dictionary[target-n], i]
            working_dictionary[n] = i
            
    print(twoSum([3, 2, 4], 6))
    print(twoSum([2,7,11,15], 26))
    print(twoSum([3,3], 6))


# Slightly different solution no enumerate.

class Solution:
    def twoSum(num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i + 1
            else:
                return map[num[i]], i + 1

        return -1, -1
    
    print(twoSum([3, 2, 4], 6))
    print(twoSum([2,7,11,15], 26))
    print(twoSum([3,3], 6))


# Nested For Loop Solution.

class Solution:
    def twoSum(nums, target):
        output = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    output.append(i)
                    output.append(j)
        return output
    
    print(twoSum([3, 2, 4], 6))
    print(twoSum([2,7,11,15], 26))
    print(twoSum([3,3], 6))
    
    
# Leetcode sends test cases as an object for their efficiency... Example of passing an object below
# However neeeds self passed through function to work for class solution

# solution = Solution()

# print(solution.twoSum([3,2,4], 6))