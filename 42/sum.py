"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""


# 1 - solution.
def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return sorted([array[i], array[j]])

    return []


# 2 - solution
def twoNumberSum2(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        CurrentSum = array[left] + array[right]

        if CurrentSum == targetSum:
            return sorted([array[left], array[right]])
        elif CurrentSum < targetSum:
            left += 1
        else:
            right -= 1

    return []
