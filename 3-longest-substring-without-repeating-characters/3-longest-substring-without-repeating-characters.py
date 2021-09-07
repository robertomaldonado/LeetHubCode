class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Get the lenght of the longest substring with no repeating chars
        Args:
            s (string)
        Returns: 
            ans (int): Count for the longest non-repeatin substring
        
        def is_valid(s):
            seen = set()
            for c in s: 
                if c in seen:
                    return False
                else:
                    seen.add(c)
            return True
            
        i, j = 0, 0
        global_sum = 0
        #We use letters so...
        letters =[0 for letter in range(0, 200)]
        string_letters =[c for c in s]
#         Now keep track of the program
        n = len(s)
        if n == 1 or n == 0:
            return n
        while i<=n and j<=n:  
            letter = string_letters[i]
            sub_str = "".join(string_letters[i:j])
            if is_valid( sub_str ) :
                letters[ord(letter)] = 1
                if len(sub_str) > global_sum:
                    global_sum = len(sub_str)
                j+=1
            else:
                i+=1
            # print(sub_str)

        return global_sum
        """
        n = len(s)
        set_ = set()
        ans, i ,j = set(), 0, 0
        
        if n == 1 or n == 0:
            return n
        
        while i<n and j<n:
            if not s[j] in set_:
                set_.add(s[j])
                j+=1
                ans.add(j-i)
            else: 
                set_.remove( s[i] )
                i+=1

        return max(ans)
            