#https://leetcode.com/contest/biweekly-contest-76/problems/maximum-score-of-a-node-sequence/
from typing import Optional
from typing import List

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        gr = []
        for i in range(n):
            gr.append([])
        #Создаем граф, в вершинах храним масси кортеджей (вес, номер вершины)
        for t in edges:
            a = t[0]
            b = t[1]
            gr[a].append((scores[b], b))  
            gr[b].append((scores[a], a))
        
        #сортируем по убыванию
        for ch in gr:
            ch.sort(reverse=True)

        res = -1
        # перебираем ребра. Пытаемся нарастить каждое ребро еще одним ребром 
        # с левого и правого конца. Если получится нарастить , то получим путь длинной 4
        for t in edges:
            a = t[0]
            b = t[1]
            n0 = len(gr[a])
            n1 = len(gr[b])
            if (n0 < 2 or n1 < 2):
                continue
            temp = scores[a] + scores[b]
            it0 = 0
            if (gr[a][it0][1] == b):  #не повезло, попали на вершину b
                it0 += 1
            temp += gr[a][it0][0]   

            it1 = 0
            if (gr[b][it1][1] == a): #не повезло, попали на вершину b
                it1 += 1

            if (gr[a][it0][1] == gr[b][it1][1]): #прямо совсем не везет, новые вершины совпали   
                #попробуем сдвинуть потомка вершины b
                it1 += 1
                if (it1 != n1 and gr[b][it1][1] == a): #опять засада
                    it1 += 1

                if (it1 != n1): #можно попробовать такой вариант
                    res = max(res,(temp + gr[b][it1][0]))    

                #попробуем сдвинуть потомка вершины a    
                it0 += 1
                if (it0 != n0 and gr[a][it0][1] == b): #опять засада
                    it0 += 1

                if (it0 != n0): #можно попробовать такой вариант
                    res = max(res,(temp + gr[a][it0][0]))    
            else:
                res = max(res,(temp + gr[b][it1][0]))

        return res




scores = [5,2,9,8,4]
edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
sol = Solution()
res = sol.maximumScore(scores, edges)
print(res)