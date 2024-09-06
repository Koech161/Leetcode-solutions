class Solution1:
    # Given an array of integers nums and an integer target,
    # return indices of the two numbers such that they add up to target.
    def twoSum(self, nums, target: int):
        num_in_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_in_index:
                return [num_in_index[complement], i]
            num_in_index[num] = i
        return None 
    
class Solution2:
#     Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


    def findMedianSortedArrays(self, nums1, nums2) -> float:

        merged = sorted(nums1 +nums2)
        length = len(merged)

        if length % 2 == 1:

         return float(merged[length //2])
        else:
         
         mid1 = length // 2 -1
         mid2 = length // 2
         return (merged[mid1] + merged[mid2])  / 2

class Solution3:
#     Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x    
        rev = 0
        while(x > 0):
            y = x % 10
            rev = rev * 10 + y
            x = x // 10
        return rev == original         
    
class Solution4:
    #Integer to Roman
    def intToRoman(self, num: int) -> str:
        roman_to_integer= [ (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        results = ''
        for value, symbol in roman_to_integer:
            while num >= value:
                results += symbol
                num -= value

        return results     

class Solution5:
    #. Roman to Integer
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'M': 1000,'D': 500, 'C': 100,'L': 50,'X': 10,'V': 5, 'I': 1
        }

        results = 0
        prev_value = 0

        for i in reversed(s):
            value = roman_to_int[i]
            if value < prev_value:
                results -= value
            else:
                results += value
                prev_value = value    
        return results     