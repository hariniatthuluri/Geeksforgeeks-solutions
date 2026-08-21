class Solution:
    def canSplit(self, arr):
        #code here
        tot=sum(arr)
        if tot%2!=0 :
            return False
        target=tot//2
        curr=0
        for x in arr:
            curr+=x
            if curr==target:
                return True
        return False