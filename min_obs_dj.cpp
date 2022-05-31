//https://leetcode.com/contest/weekly-contest-295/problems/minimum-obstacle-removal-to-reach-corner/
#include <iostream>
#include <vector>
#include <set>
using namespace std;
//Алгоритм Дейкстры

class Solution
{
public:
    int minimumObstacles(vector<vector<int>> &grid)
    {
        int m = grid.size();
        int n = grid[0].size();
        int l = n * m;
        vector<int> d(l, -1);

        vector<pair<int, int>> shift;

        shift.push_back(make_pair(-1, 0));
        shift.push_back(make_pair(1, 0));
        shift.push_back(make_pair(0, -1));
        shift.push_back(make_pair(0, 1));

        //Алгоритм Дейкстры
        set<pair<int, pair<int, int>>> q;
        d[0] = 0;
        q.insert(make_pair(d[0], make_pair(0, 0)));
        while (!q.empty())
        {
            pair<int, int> xy = q.begin()->second;
            q.erase(q.begin());
            int v = xy.first * n + xy.second;
            for (int i = 0; i < 4; i++)
            {
                int x = xy.first + shift[i].first;
                int y = xy.second + shift[i].second;
                if (x > -1 && x < m && y > -1 && y < n)
                {
                    int t = x * n + y;
                    int w = grid[x][y];
                    if ((d[t] == -1) || (d[t] > d[v] + w))
                    {
                        if (d[t] > 0)
                            q.erase(make_pair(d[t], make_pair(x, y)));
                        d[t] = d[v] + w;
                        q.insert(make_pair(d[t], make_pair(x, y)));
                    }
                }
            }
        }

        return d[l - 1];
    }
};

int main()
{
    vector<vector<int>> grid = {{0, 0, 1, 1, 1, 1, 0, 0, 0, 1}, {0, 1, 1, 1, 1, 1, 1, 0, 1, 1}, {1, 1, 0, 1, 1, 1, 1, 0, 1, 0}, {0, 0, 1, 1, 1, 1, 0, 0, 1, 1}, {1, 0, 1, 0, 0, 0, 1, 1, 1, 0}};
    Solution sol;
    int res = sol.minimumObstacles(grid);
    cout << res;
}