class Solution:
    def maxWater(self, arr):
        # code here
        left=0
        right=len(arr)-1
        ans=0
        
        while left<right:
            height=min(arr[left],arr[right])
            width=right-left
            
            ans=max(ans,width*height)
            
            if arr[left]<arr[right]:
                left+=1
            else:
                right-=1
                
        return ans