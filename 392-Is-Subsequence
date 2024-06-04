def isSubsequence(self, s: str, t: str) -> bool:
        
        sidx = 0
        tidx = 0
            
        if len(s) > len(t):
           
            return False
        
        while sidx < len(s) and tidx < len(t):
            
            if s[sidx] == t[tidx]:
               
                sidx += 1
            tidx += 1
        if sidx == len(s):
            return True 
        else: 
            return False