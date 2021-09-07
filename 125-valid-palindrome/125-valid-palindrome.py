class Solution:
    def isPalindrome(self, s: str) -> bool:
      """ 
      (str) -> bool
  
      Return True if and only if s is a palindrome.
      """
  
      # s[i] and s[j] are the next pair of characters to compare.
      s = "".join([c.lower() for c in s if c not in string.punctuation and c != " "])
      
      i = 0
      j = len(s) - 1
  
      # The characters in s[:i] have been successfully compared to those in s[j:].
      while i < j and s[i] == s[j]:
          i += 1
          j -= 1
  
      # If we exited because we successfully compared all pairs of characters,
      # then j <= i.
      return i >= j