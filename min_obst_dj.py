# https://leetcode.com/contest/weekly-contest-295/problems/minimum-obstacle-removal-to-reach-corner/
from typing import Optional
from typing import List
from sortedcontainers import SortedList


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        l = n*m

        shift = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # ищем кратчайший путь в gr алгоритмом Дейкстры
        dist = [-1]*l
        tree = SortedList()
        dist[0] = 0
        tree.add((0, (0, 0)))
        while len(tree) > 0:
            vp = tree.pop(0)
            xy = vp[1]  # номер вершины
            v = xy[0] * n + xy[1]
            for u in shift:  # перебираем вершины
                x = xy[0] + u[0]
                y = xy[1] + u[1]
                if (x > -1 and x < m and y > -1 and y < n):
                    t = x * n + y  # номер вершины
                    w = grid[x][y]  # вес вершины
                    if ((dist[t] == -1) or (dist[t] > dist[v] + w)):
                        if (dist[t] > 0):
                            tree.remove((dist[t], (x, y)))
                        dist[t] = dist[v] + w
                        tree.add((dist[t], (x, y)))

        return dist[l-1]  # возвращаем растояние до последней точки


a = [[0, 0, 1, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 0, 1,
                                                                      1, 1, 1, 0, 1, 0], [0, 0, 1, 1, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 0, 0, 1, 1, 1, 0]]
#a = [[0,1,1,1,0]]
#a = [[0,1,1,1,1,1,0,1],[0,1,1,1,1,1,0,1],[1,1,1,1,0,0,0,1],[1,1,1,1,1,1,1,1],[0,1,1,0,0,0,0,1],[1,1,1,1,1,1,0,0]]
#a = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
#a = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
sol = Solution()
res = sol.minimumObstacles(a)
print(res)
