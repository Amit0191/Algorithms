from typing import List
    
def binary_search(nums:List[int], key: int) -> int:
    l = 0
    h = len(nums)

    while l < h:
        m = (l + h)//2
        
        if nums[m] == key:
            return m
        elif key < nums[m]:
            h = m - 1
        else:
            l = m + 1
    return -1


a = [5, 4, 7, 2, 1, 9]
print(binary_search(a, 9))
