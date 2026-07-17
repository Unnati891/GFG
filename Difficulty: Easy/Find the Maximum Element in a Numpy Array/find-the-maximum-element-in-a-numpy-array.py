import math
class Solution:
    def maxElement(self, arr):
       x = -math.inf
       for i in arr:
           if i>x:
               x=i
       return x;
        