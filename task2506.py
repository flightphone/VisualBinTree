from typing import Optional
from typing import List
from sortedcontainers import SortedList

class Solution:
    #https://leetcode.com/problems/create-sorted-array-through-instructions/

    #https://leetcode.com/problems/count-good-triplets-in-an-array/
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:    
        res = 0
        n = len(nums1)
        inx = [0]*n
        for i in range(n):
            inx[nums2[i]] = i
        tree_l = SortedList()
        tree_r = SortedList(nums2)
        a = inx[nums1[0]]
        tree_r.remove(a)
        tree_l.add(a)
        for i in range(1, n-1):
            a = inx[nums1[i]]
            tree_r.remove(a)
            k_r = len(tree_r) -tree_r.bisect_right(a)
            k_l = tree_l.bisect_right(a)
            res = res + k_r * k_l
            tree_l.add(a)

        return res

    #https://leetcode.com/problems/maximize-score-after-n-operations/
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tree = SortedList()
        n = len(nums)
        for a in nums:
            tree.add(-a)
        ans = [0]*n
        for i in range(n):
            k = tree.bisect_right(-nums[i])
            ans[i] = n - k
        return ans        

    #https://leetcode.com/problems/count-of-range-sum/
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pref = 0
        res = 0
        tree = SortedList()
        tree.add(pref)
        for a in nums:
            pref += a
            k = tree.bisect_left(pref - upper)
            k2 = tree.bisect_right(pref - lower)
            tree.add(pref)
            res = res + k2 - k
        return res


    #https://leetcode.com/problems/reverse-pairs/
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tree = SortedList()
        res = 0
        for i in range(n):
            k = tree.bisect_right(2 * nums[i])
            res = res + len(tree) - k
            tree.add(nums[i])
        return res



    #https://leetcode.com/problems/count-of-smaller-numbers-after-self/
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        tree = SortedList()
        for i in range(n):
            j = n - 1 - i
            k = tree.bisect_right(-nums[j])
            ans[j] = len(tree) - k
            tree.add(-nums[j])
        return ans


    #https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        k = n // 2
        nums.sort()
        res = 0
        for i in range(k):
            res = res + nums[n-1-i] - nums[i]
        return res

    #https://leetcode.com/problems/queue-reconstruction-by-height/
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:    
        n = len(people)
        people.sort(key=lambda a: (a[0],-a[1])) 
        ans = [[0, 0]]*n
        tree = SortedList()
        for i in range(n):
            tree.add(i)
        for a in people:
            i = a[1]
            k = tree[i]
            ans[k] = a
            tree.remove(k)
        return ans 

    # https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
    def minDeletions(self, s: str) -> int:
        c = dict()
        for a in s:
            f = c.get(a, 0)
            f += 1
            c[a] = f

        n = len(s)
        dif = [0]*(n+1)
        for key in c:
            f = c[key]
            dif[f] = dif[f] + 1

        res = 0
        for i in range(n):
            j = n - i
            nf = dif[j]
            if nf < 2:
                continue    
            res = res + nf - 1
            dif[j-1] = dif[j-1] + nf - 1

        return res    


    # https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
    def minPartitions(self, n: str) -> int:
        l = len(n)
        ans = 0
        for i in range(l):
            a = n[i]
            ans = max(ans, ((ord(a) - ord("1")) + 1))
        return ans

    # https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        pref = [0]*(n+1)
        for i in range(1, n+1):
            pref[i] = pref[i-1] + cardPoints[i-1]

        minSum = pref[n]
        if k == n:
            return minSum

        l = n-k
        for i in range(k+1):
            i2 = i+l
            minSum = min(minSum, (pref[i2] - pref[i]))

        return pref[n] - minSum

    # https://leetcode.com/problems/non-decreasing-array/

    def checkPossibility(self, nums: List[int]) -> bool:
        check = 0
        n = len(nums)
        for i in range(1, n):
            if (nums[i] < nums[i-1]):
                a = -200000
                if i > 1:
                    a = nums[i-2]
                if (nums[i] < a):
                    # увеличиваем i
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]

                check += 1
                if (check > 1):
                    return False

        return True


'''
sol = Solution()
nums = [5,7,1,8]
r = sol.checkPossibility(nums)
print(r)
'''


'''
cardPoints = [9, 7, 7, 9, 7, 7, 9]
k = 7
r = sol.maxScore(cardPoints, k)
'''
'''
s = "ceabaacb"
r = sol.minDeletions(s)
print(r)
'''
'''
sol = Solution()
people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
ans = sol.reconstructQueue(people)
print(ans)
'''

'''
sol = Solution()
nums = [1,10,2,9]
r = sol.minMoves2(nums)
print(r)
'''
'''
nums = [1,2,3,4,5]
sol = Solution()
ans = sol.reversePairs(nums)
#ans = sol.countSmaller(nums)
print(ans)
'''
'''
nums = [0]
lower = 0
upper = 0
sol = Solution()
r = sol.countRangeSum(nums, lower, upper)
print(r)
'''
'''
nums = [7,7,7,7]
sol = Solution()
ans = sol.smallerNumbersThanCurrent(nums)
print(ans)
'''
sol = Solution()
nums1 = [4,0,1,3,2]
nums2 = [4,1,0,2,3]
r = sol.goodTriplets(nums1, nums2)
print(r)