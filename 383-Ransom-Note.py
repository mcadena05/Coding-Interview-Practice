def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dic = {}
        mag_dic = {}

        for char in ransomNote:
            if char not in ransom_dic:
                ransom_dic[char] = 1
            else:
                ransom_dic[char] += 1
        
        for char in magazine:
            if char not in mag_dic:
                mag_dic[char] = 1
            else:
                mag_dic[char] += 1
        
        for char in ransomNote:
            if char not in mag_dic:
                return False
            elif ransom_dic[char] != mag_dic[char]:
                return False
            else:
                return True