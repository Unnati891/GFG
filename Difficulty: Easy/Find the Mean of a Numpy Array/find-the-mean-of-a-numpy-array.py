class Solution:
    def arrayMean(self, arr):
        n=len(arr)
        total=0
        for i in arr:
            total+=i;
        avg=total/n
        return avg