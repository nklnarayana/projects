import collections

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        dq = collections.deque()
        ans = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            # if the position of the maximum number is outside the current window , then delete(popelft from dequeu)
            if dq[0] == i - k:
                print 'popleft'
                print 'dq[0] is %d' %dq[0]
                print 'i is %d' %i
                print 'k is %d' %k
                dq.popleft()
            if i >= k - 1:
                ans.append(nums[dq[0]])
        return ans


s = Solution()
print s.maxSlidingWindow([3,2,-1,0,5,3,8,6,7,11],3)



