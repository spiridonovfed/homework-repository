"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    for index in range(len(nums) - k + 1):
        candidate_sum = sum(nums[index : index + k])
        if candidate_sum > max_sum:
            max_sum = candidate_sum
    return max_sum
