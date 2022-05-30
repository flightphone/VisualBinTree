//https://leetcode.com/contest/weekly-contest-295/problems/minimum-obstacle-removal-to-reach-corner/
#include <iostream>
#include <vector>
#include <set>
using namespace std;
//Алгоритм Дейкстры

class Solution
{
public:
    void addV(int x1, int y1, int x2, int y2, int n, vector<vector<int>> &grid, vector<vector<pair<int, int>>> &gr)
    {
        int v1 = x1 * n + y1;
        int v2 = x2 * n + y2;
        int w1 = grid[x1][y1]; //веса вершин
        int w2 = grid[x2][y2]; //веса вершин
        gr[v2].push_back(make_pair(v1, w1));
        gr[v1].push_back(make_pair(v2, w2));
    }

    int minimumObstacles(vector<vector<int>> &grid)
    {
        int m = grid.size();
        int n = grid[0].size();
        int l = n * m;
        vector<vector<pair<int, int>>> gr(l);
        vector<int> d(l, -1);
        //Формируем граф с весами 0-1
        for (int x = 0; x < m; x++)
            for (int y = 0; y < n; y++)
            {
                if (x > 0)
                    addV(x - 1, y, x, y, n, grid, gr);
                if (y > 0)
                    addV(x, y - 1, x, y, n, grid, gr);
            }

        //Алгоритм Дейкстры
        set<pair<int, int>> q;
        d[0] = 0;
        q.insert(make_pair(d[0], 0));
        while (!q.empty())
        {
            int v = q.begin()->second;
            q.erase(q.begin());
            int nc = gr[v].size();
            for (int i = 0; i < nc; i++)
            {
                int t = gr[v][i].first;
                int w = gr[v][i].second;
                if ((d[t] == -1) || (d[t] > d[v] + w))
                {
                    if (d[t] > 0)
                        q.erase(make_pair(d[t], t));
                    d[t] = d[v] + w;
                    q.insert(make_pair(d[t], t));
                }
            }
        }

        return d[l-1];
    }
};


int main()
{
   vector<vector<int>> grid = {{0,0,1,1,1,1,0,0,0,1},{0,1,1,1,1,1,1,0,1,1},{1,1,0,1,1,1,1,0,1,0},{0,0,1,1,1,1,0,0,1,1},{1,0,1,0,0,0,1,1,1,0}};  
   Solution sol;
   int res = sol.minimumObstacles(grid);
   cout << res;
}