def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        ans = 0
        while(x>0):
            ans = ans *10 + x%10
            x //= 10 
        print("temp", temp)
        print("ans", ans)
        return temp == ans