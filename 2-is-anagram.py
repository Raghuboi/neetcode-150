class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        
        countS, countT = {}, {}
        
        for index in range(len(s)):
            countS[s[index]] = countS.get(s[index], 0) + 1
            countT[t[index]] = countT.get(t[index], 0) + 1
        
        return countS == countT


if __name__ == '__main__':
    solution = Solution()

    assert solution.isAnagram("racecar", "carrace") == True
    assert solution.isAnagram("jar", "jam") == False

    print("All tests passed!")
