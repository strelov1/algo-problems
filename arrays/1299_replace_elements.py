#1299. Replace Elements with Greatest Element on Right Side
# O(n) | Space: O(1)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        for i in range(size):
            slice = arr[i+1:size]
            if len(slice):
                arr[i] = max(arr[i+1:size])
            if i == size-1:
                arr[i] = -1
            
        return arr