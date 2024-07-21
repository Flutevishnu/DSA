class Solution:
    def lengthOfLongestSubstring(self, s: str):
        arr = []
        
        for i in range(len(s)):
            temp = ""
            for j in range(i, len(s)):
                if s[j] not in temp:
                    temp += s[j]
                else:
                    break
            print(temp)
            arr.append(temp)
        
        maax = 0
        for i in arr:
            maax = max(maax, len(i))
        return maax
                                 

