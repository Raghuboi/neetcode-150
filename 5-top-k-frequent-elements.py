from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequencies = defaultdict(list)
        result = []
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1            
            
        for num, count in counts.items():
            frequencies[count].append(num)
            
        for frequency in range(len(nums), 0, -1):
            if frequency in frequencies:
                result.extend(frequencies[frequency])
                if (len(result) >= k):
                    return result[:k]
                
        return result


if __name__ == '__main__':
    solution = Solution()

    # Test 1: nums = [1,2,2,3,3,3], k = 2
    # Frequencies: 1 appears 1x, 2 appears 2x, 3 appears 3x
    # Top 2 frequent: 3 and 2
    result1 = solution.topKFrequent([1, 2, 2, 3, 3, 3], 2)
    assert set(result1) == {2, 3}

    # Test 2: nums = [7,7], k = 1
    # Top 1 frequent: 7
    result2 = solution.topKFrequent([7, 7], 1)
    assert result2 == [7]

    print("All tests passed!")
