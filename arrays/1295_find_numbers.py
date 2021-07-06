# O(n) | Space: O(1)
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                counter += 1
            
        return counter