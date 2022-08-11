from typing import Optional
from typing import List


class FenwickTree:
    def __init__(self, size):
        self._array = [0] * (size + 1)
        self._current = [0] * (size + 1)
        self.Count =  size
        self.logn = 1
        while (self.logn * 2 < self.Count):
            self.logn *= 2
        
    def Add(self, i, n):
        self._current[i] = self._current[i] + n
        i += 1
        while  (i <= self.Count):
            self._array[i] = self._array[i] + n
            i += (i & -i)
    
    def update(self, i, n):
        val = self._current[i]
        self.Add(i, (n - val))

    def Sum(self, r):
        result = 0
        while (r > 0):
            result += self._array[r]
            r -= (r & -r)
        return result

    def LowerBound(self, w):
        if w <= 0:
            return 0
        x = 0
        k = self.logn
        while k > 0:    
            if (x + k < self.Count and self._array[x + k] < w):
                w -= self._array[x + k]
                x += k
            k = k // 2
        return (x+1)                

class FenwickTree_Max:
    def __init__(self, size) -> None:
        self.n = size
        self.INF = 0
        self.t = [self.INF]*size
    
    def getMax(self, r):
        if r < 0:
            r = 0
        if r > (self.n-1):
            r = self.n - 1
        result = self.INF
        while r >= 0:
            result = max(result, self.t[r])            
            r = (r & (r + 1)) - 1
        return result
    
    def update(self, i, new_val):
        while i < self.n:
            self.t[i] = max(self.t[i], new_val)
            i = (i | (i + 1))

class Solution:
    #https://leetcode.com/problems/longest-increasing-subsequence/
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        fm = FenwickTree_Max(20009)
        k = 1
        for i in range(n):
            nums[i] = nums[i] + 10000
            a = fm.getMax(nums[i]-1) + 1
            fm.update(nums[i], a)
            k = max(a, k);
        return k

#https://leetcode.com/problems/range-sum-query-mutable/
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.ft = FenwickTree(n)
        for i in range(n):
            self.ft.Add(i, nums[i])
        

    def update(self, index: int, val: int) -> None:
        self.ft.update(index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        a1 = self.ft.Sum((right + 1))
        a2 = self.ft.Sum((left))
        return (a1 - a2)



nums = [0,1,0,3,2,3]
sol = Solution()
r = sol.lengthOfLIS(nums)
print(r)
'''
ft = FenwickTree(10)
ft.Add(0, 1)
ft.Add(9, 1)
r = ft.Sum(10)
print(r)
ft.Add(3, 1)
ft.Add(4, 1)
ft.Add(5, 1)
r = ft.Sum(5)
print(r)

f = ft.LowerBound(5)
print(f)
'''