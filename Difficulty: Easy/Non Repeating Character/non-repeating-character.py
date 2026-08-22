class Solution:
    def nonRepeatingChar(self,s):
        #code here
        freq={}
        
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
            
        for ch in s:
            if freq[ch]==1:
                return ch
                
        return '$'