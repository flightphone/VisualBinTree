#https://leetcode.com/contest/weekly-contest-290/problems/count-number-of-rectangles-containing-each-point/
from typing import List
from sortedcontainers import SortedList

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        
        #сортируем точки
        po = []
        n = len(points)    
        for i in range(n):
            p = points[i]
            po.append((p[0], p[1], i))   
        po = sorted(po)        

        

        #дерево по y
        tree_y = SortedList()
        for r in rectangles:
            tree_y.add((r[1], r[0]))  #добавляем в дерево y,x

        #сортируем прямоугольники
        n = len(rectangles)
        rectangles = sorted(rectangles)
        
        
        # перебираем отсортированные точки, по ходу перебора отпиливаем от дерева больше ненужные 
        # вершины слева от текщей точки , используем текущий указатель start
        start = 0
        res = [0] * len(points)
        for p in po:

            i = p[2]
            #удаляем из дерева левые элементы, все точки с координатой строго меньше 
            # координаты текущей точки p
            a = [p[0], p[1]]
            while (start < n and rectangles[start] < a):
                dl = (rectangles[start][1], rectangles[start][0])
                tree_y.remove(dl)
                start += 1    

            find = (p[1], -1)    
            ind = tree_y.bisect_left(find) # если ничего не нашли, то ind = -1
            if (ind > -1):
                res[i] = len(tree_y) - ind

        return res



rectangles = [[1,10],[10,1]]
points = [[5,5],[1,1]]
sol = Solution()
res = sol.countRectangles(rectangles, points)
print(res)