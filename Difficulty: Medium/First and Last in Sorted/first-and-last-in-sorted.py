class Solution:
    def find(self, arr, x):
        # code here
        ans=[]
        for i in range(len(arr)):
            if arr[i]==x:
                ans.append(i)
        if len(ans)>0:
            return [min(ans),max(ans)]
        return [-1,-1]