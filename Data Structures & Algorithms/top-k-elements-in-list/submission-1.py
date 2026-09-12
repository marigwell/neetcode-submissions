import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: list of integers nums, and integer k
        # output: list containing the k most frequent nums
        freq = {}

        # max heap
        heap = []

        result = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))

        for _ in range(k):
            count, num = heapq.heappop(heap)
            result.append(num)
        return result