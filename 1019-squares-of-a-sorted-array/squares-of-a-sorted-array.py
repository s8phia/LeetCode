class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squaredArray = []
        for num in nums:
            squaredArray.append(num ** 2)
        squaredArray.sort()
        return squaredArray

        
        