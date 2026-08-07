class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def func(nums,goal):
            if(goal<0):
                return 0
            sum=0
            count=0
            left,right=0,0
            n=len(nums)
            while(right<n):
                sum+=nums[right]
                while(sum>goal):
                    sum-=nums[left]
                    left+=1
                count+=right-left+1
                right+=1
            return count
        return func(nums,goal)-func(nums,goal-1)
