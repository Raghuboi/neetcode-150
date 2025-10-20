from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass


if __name__ == '__main__':
    solution = Solution()

    result1 = solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
    expected1 = [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]
    assert set(frozenset(group) for group in result1) == set(frozenset(group) for group in expected1)

    result2 = solution.groupAnagrams(["x"])
    expected2 = [["x"]]
    assert set(frozenset(group) for group in result2) == set(frozenset(group) for group in expected2)

    print("All tests passed!")
