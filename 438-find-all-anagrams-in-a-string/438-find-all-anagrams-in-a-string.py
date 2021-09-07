class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        def char_index(c):
            if len(c) == 1:
                val = ord(c)-ord('a')
                if val >= 0 and val < 26:
                    return val
            return -1
        results = []
        
        # If either string is empty or p is longer than s, we have no results
        if len(s) == 0 or len(p) == 0 or len(s) < len(p): return results

        # Counts of characters. We are told that all chars are lowercase English
        # characters
        p_chars = [0]*26
        for c in p:
            p_chars[char_index(c)] = p_chars[char_index(c)]+1

        # Track the start and end of our window in s, along with the chars in that
        # window. This should always be the size of p
        start = 0
        end = len(p)-1;
        s_chars = [0]*26

        # Fill up initial s_chars
        for i in range(len(p)):
            s_chars[char_index(s[i])] = s_chars[char_index(s[i])]+1

        # Iterate through every substring of length p
        while end < len(s)-1:
            # This is a slow but constant time operation because the arrays are
            # always the same size ragardless of the input
            if (all(s_chars[i] == p_chars[i] for i in range(len(s_chars)))):
                results.append(start)

            # Move our window by 1
            s_chars[char_index(s[start])] = s_chars[char_index(s[start])]-1
            start = start+1
            end = end+1
            s_chars[char_index(s[end])] = s_chars[char_index(s[end])]+1

    # Get the last substring if it's valid
        if (all(s_chars[i] == p_chars[i] for i in range(len(s_chars)))):
            results.append(start)

        return results