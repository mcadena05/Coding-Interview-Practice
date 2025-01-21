def isIsomorphic(self, s: str, t: str) -> bool:
    dict = {}
    for i, char in enumerate(s):
            
            # dict[s[0]] = t[0]
            # print(dict)

         if char not in dict.keys():
             if t[i] in dict.values():
                return False
             else:
                dict[s[i]] = t[i]
                print(dict)
         else:
            if dict[char] != t[i]:
                return False
    return True