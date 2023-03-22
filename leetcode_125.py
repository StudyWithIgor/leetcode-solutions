'''
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
O(n) time O(1) space
n=number of characters in input string
'''

class Solution(object):
    def isPalindrome(self,s):
        left=0
        right=len(s)-1


        while left<right:
            while left<right and not s[left].isalnum():
                left+=1

            while left<right and not s[right].isalnum():
                right-=1

            if left<right and s[left].lower()!=s[right].lower():
                return False
            else:
                left+=1
                right-=1

        return True
