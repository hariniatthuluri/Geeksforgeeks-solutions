class Solution:
    def visibleBuildings(self, arr):
        # code here
        count=0
        max_height=0
        for i in range(len(arr)):
            if arr[i]>=max_height:
                count+=1
                max_height=arr[i]
        return count