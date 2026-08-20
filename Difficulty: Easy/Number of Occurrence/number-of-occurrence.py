class Solution:
    def countFreq(self, arr, target):
        n=len(arr)
        low,high=0,len(arr)-1
        first=-1
        while low<=high:
            mid=(low+high)//2
            if target==arr[mid]:
                first=mid
                high=mid-1
            elif target>arr[mid]:
                low=mid+1
            else:
                high=mid-1
                
        if first==-1:
            return 0
        
        low,high=0,n-1
        last=-1
        while low<=high:
            mid=(low+high)//2
            if target==arr[mid]:
                last=mid
                low=mid+1
            elif target>arr[mid]:
                low=mid+1
            else:
                high=mid-1
        return last-first+1