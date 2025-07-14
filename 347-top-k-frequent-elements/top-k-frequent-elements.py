class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = defaultdict(int)
        amount = []

        for num in nums:
            frequent[num] += 1
        sorted_items = sorted(frequent.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            amount.append(sorted_items[i][0])
        
        return amount
                