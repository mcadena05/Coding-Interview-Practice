class Solution:
    def isPalindrome(self, s: str) -> bool:
        # nonAlpha = [' ', ',', '.', '!', '?',':', '@', '#', '_']
        # newString = ''

        # for char in s:
        #     if char not in nonAlpha:
        #         newString += char

        # s = ''.join(filter(str.isalnum, input))      
        # lowerStr = newString.lower()
        # reverse = lowerStr[::-1]
        
        # if reverse == lowerStr:
        #     return True
        # else:
        #     return False


        filtered = filter(lambda ch: ch.isalnum(), s)
        lowerFiltered= map(lambda ch: ch.lower(), filtered)

        filtered_chars_list = list(lowerFiltered)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list