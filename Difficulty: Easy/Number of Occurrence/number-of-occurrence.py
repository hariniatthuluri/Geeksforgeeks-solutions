class Solution:
    def countFreq(self, arr, target):
        res=[]
        for i in range(len(arr)):
            if arr[i]==target:
                res.append(i)
        return (len(res))