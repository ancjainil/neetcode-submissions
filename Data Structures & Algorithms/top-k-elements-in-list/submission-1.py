class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        cntMap = Counter(nums)

        for num,cnt in cntMap.items():
            heapq.heappush(minHeap, [cnt,num])
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        res =[]
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res
        