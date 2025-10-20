from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    # Alternative: One-liner (most concise)
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     return len(nums) != len(set(nums))

if __name__ == '__main__':
    solution = Solution()

    assert solution.hasDuplicate([1, 2, 3, 3]) == True
    assert solution.hasDuplicate([1, 2, 3, 4]) == False

    print("All tests passed!")
