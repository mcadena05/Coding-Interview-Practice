def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        
        for i in range(len(str_x)-1):  
            print(i)
            for j in range(len(str_x)-1, i, -1):
                if str_x[j] != str_x[i]:
                    return False
                else:
                    return True
                i += 1