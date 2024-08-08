def isPalindrome(x: int) -> bool:
        if x < 0:
            return "false"
        temp = x
        ans = 0
        while(x>0):
            num = x%10
            ans = ans *10 + num
            x //= 10 
        print("temp", temp)
        print("ans", ans)
        return temp == ans
print(isPalindrome(-121))
