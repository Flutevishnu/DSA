s = "anagram"
t = "nagaram"
countS = {}
countT = {}
for i in range(len(s)):
    countS[s[i]] = 1 + countS.get(s[i], 0)
    countT[t[i]] = 1 + countT.get(t[i], 0)
print(countT == countS)