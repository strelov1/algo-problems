#961. N-Repeated Element in Size 2N Array
# O(n) | Space: O(n)
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = {}
        for n in nums:
            if n in seen:
                return n
            seen[n] = True
        
        return False