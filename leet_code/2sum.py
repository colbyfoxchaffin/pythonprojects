#Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Brute Force
def twoSumBruteForce(nums, target):
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if num + nums[j] == target:
                return [i,j]

#Hash Map
def twoSumHashMap(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if target - num in dic:
            return [i, dic[target - num]]
        dic[num] = i

#Binary Search Solution
#Returns -1 if no target is found
# def twoSumBinSearch(nums, target):
#     nums.sort()

#     for i, num in enumerate(nums):
#         index = binary_search(target - num, nums)
#         if index != -1:
#             return [i, index]
