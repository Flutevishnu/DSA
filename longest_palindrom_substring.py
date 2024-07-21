def longestPalindrome(s: str) -> str:
        arr = [] 
        for i in range(len(s)):
            temp = ""
            for j in range(i, len(s)):
                temp += s[j]
                if temp == temp[::-1]:
                    arr.append(temp)
                else:
                    
        print(arr)
print(longestPalindrome("babad"))