from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += f"{len(s)}#{s}"
        return output
    
    def decode(self, s: str) -> List[str]:
        output = []
        counter = 0
        
        while counter < len(s):
            symbol_pos = counter           
            while s[symbol_pos] != "#":
                symbol_pos += 1
            length = int(s[counter:symbol_pos])
            
            start = symbol_pos + 1
            word = s[start:start+length]
            output.append(word)
            
            counter = start + length
        
        return output
            
if __name__ == '__main__':
    solution = Solution()

    # Test 1: ["neet","code","love","you"]
    test1 = ["neet", "code", "love", "you"]
    encoded1 = solution.encode(test1)
    decoded1 = solution.decode(encoded1)
    assert decoded1 == test1, f"Expected {test1}, got {decoded1}"

    # Test 2: ["we","say",":","yes"] - tests special character handling
    test2 = ["we", "say", ":", "yes"]
    encoded2 = solution.encode(test2)
    decoded2 = solution.decode(encoded2)
    assert decoded2 == test2, f"Expected {test2}, got {decoded2}"

    print("All tests passed!")
