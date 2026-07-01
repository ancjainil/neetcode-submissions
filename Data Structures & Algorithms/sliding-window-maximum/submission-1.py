class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if not nums or k<=0:
            return []
        if k==1:
            return nums
        
        result = []
        dq = deque()
        for i in range(k):
            while dq and nums[i]>= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        
        for i in range(k, len(nums)):
            result.append(nums[dq[0]])

            while dq and dq[0]<=i-k:
                dq.popleft()

            while dq and nums[i]>= nums[dq[-1]]:
                dq.pop()
            
            dq.append(i)

        result.append(nums[dq[0]])
        return result
