class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_pad = { '2': 'abc', '3': 'def','4': 'ghi','5': 
                     'jkl','6': 'mno', '7': 'pqrs','8': 'tuv','9': 'wxyz'}
        if digits == "": 
            return []
        ans = [""]
        
        for d in digits:
            tmp = []
            for v in phone_pad[d]:
                for o in ans:
                    tmp.append(o+v)
            ans = tmp
                
        # for digit in digits[1:]:
        #     numbers = [old+new for old in numbers for new in list(phone_pad[digit])]
        return ans
    