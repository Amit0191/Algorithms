from typing import List

def selection_sort(nums: List) -> List[int]:
    """Selection sort finds the smallest element and swaps it with the ith element of the array. Where i = 0, 1, ... n-1"""
    for i in range(0, len(nums) - 1):
        min = nums[i]
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < min:
                min = nums[j]
                min_idx = j
        tmp = min
        nums[min_idx] = nums[i]
        nums[i] = tmp
    return nums


