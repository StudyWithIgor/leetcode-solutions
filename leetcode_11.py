'''
Leetcode 11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

O(n) time and O(1) space
n=number of elements in input array
'''

class Solution(object):
    def maxArea(self, arr):
        left=0
        right=len(arr)-1
        ans=0

        while left<right:
            limit=min(arr[left],arr[right])
            area=(right-left)*limit
            ans=max(ans,area)
            
            if arr[left]<=arr[right]:
                left+=1
            else:
                right-=1

        return ans
