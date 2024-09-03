def encode(strs) :
    res = ""
    for i in strs:
        res += str(len(i))+"#"+i
    return res
        

def decode(s: str) :
    print(s)
    res = []
    i = 0
    while(i<len(s)):
        j = i
        while(s[j] != "#"):
            j+=1
        length = int(s[i:j])
        print(length)
        i=j+1
        j = i+length
        res.append(s[i:j])
        i=j

    return res


print(decode(encode(["neet","code","love","you"])))