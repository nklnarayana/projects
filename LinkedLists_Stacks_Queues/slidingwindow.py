#Problem: 
#A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array to the very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position. Following is an example:
#The array is [1 3 -1 -3 5 3 6 7], and w is 3.

#Input: A long array A[], and a window width w
#Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
#Requirement: Find a good optimal way to get B[i]



# Rule is MAXIMUM element in window would be stored in front of deque
import collections

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        dq = collections.deque()
        ans = []
        for i in range(len(nums)):
            #if the element scanned is greater than element at back(right side) of deque, 
            #then pop(elemeng at back (right side)) from dequeue
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            # if the position of the maximum number is outside the current window , then delete(popelft from dequeu)
            if dq[0] == i - k:
                dq.popleft()
            if i >= k - 1:
                ans.append(nums[dq[0]])
        return ans


s = Solution()
arr = [3,2,-1,0,5,3,8,6,7,11]
print 'original array is ', arr
window_size = 3
print 'window size is %d' %window_size 
print 'sliding window is ' , s.maxSlidingWindow(arr,window_size)


#output

#python slidingwindow.py 
#original array is  [3, 2, -1, 0, 5, 3, 8, 6, 7, 11]
#window size is 3
#sliding window is  [3, 2, 5, 5, 8, 8, 8, 11]
