from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for index, num in enumerate(nums):
          difference = target - num
          solution = values.get(difference)
          if solution != None:
            return [solution, index]
          else:
            values[num] = index

if __name__ == '__main__':
    solution = Solution()

    assert solution.twoSum([3, 4, 5, 6], 7) == [0, 1]
    assert solution.twoSum([4, 5, 6], 10) == [0, 2]

    print("All tests passed!")