class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        temp = collections.deque() 
        print(temp)
        
        left = 0
        right = 0
    
        while right < len(nums):
            #print(temp)
            while len(temp) != 0 and nums[temp[-1]] < nums[right]:
                temp.pop() 
                #print(temp)
            temp.append(right)
        
            if left > temp[0]:
                #print('popl')
                temp.popleft()
        
            if right+1 >= k:
                ans.append(nums[temp[0]])
                left += 1
            right += 1
        return ans