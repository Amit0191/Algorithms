from typing import List

def insertion_sort(nums: List) -> List[int]:
    """Insertion sort compares an element with rest of the elements in the array from right to left. """
    for i in range(1, len(nums)):
        j = i - 1
        key = nums[i]
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

