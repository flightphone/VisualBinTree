using System;
using System.Linq;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace leetSharp
{

    //Дерево Фенвика

    //Декартово дерево
    public class Cartesian_item<T> where T : IComparable<T>
    {
        public T key { get; set; }
        public Guid prior { get; set; }
        public long sum = 0;
        public long ordsum = 0;
        public int cnt = 1;
        public int ord = 0;
        public long min = 0;
        public long nmin = 0;

        public long value { get; set; }


        public Cartesian_item<T> l;
        public Cartesian_item<T> r;
        public Cartesian_item()
        {
            prior = Guid.NewGuid();
            l = null;
            r = null;
        }
        public Cartesian_item(T _key, long _val)
        {
            this.key = _key;
            this.value = _val;
            this.sum = _val;
            this.min = _val;
            prior = Guid.NewGuid();
            l = null;
            r = null;
        }

        /*
             public void upd_cnt()
             {
                 cnt = 1;
                 if (l != null)
                     cnt += l.cnt;
                 if (r != null)
                     cnt += r.cnt;
             }

             public void upd_sum()
             {
                 sum = value;
                 if (l != null)
                     sum += l.sum;
                 if (r != null)
                     sum += r.sum;
             }
         */

        public void upd_min()
        {
            min = value;
            cnt = 1;
            sum = value;
            if (l != null)
            {
                min = Math.Max(min, l.min);
                cnt += l.cnt;
                sum += l.sum;

            }
            if (r != null)
            {
                min = Math.Max(min, r.min);
                cnt += r.cnt;
                sum += r.sum;
            }

            /*
            nmin = 0;
            if (l != null && min == l.min)
                nmin += l.nmin;

            if (r != null && min == r.min)
                nmin += r.nmin;

            if (min == value)
                nmin++;
            */

        }
    }

    public class Cartesian_tree<T> where T : IComparable<T>
    {
        public Cartesian_item<T> root = null;
        public void dfs()
        {
            dfs(root);
        }

        public void dfs(Cartesian_item<T> t)
        {
            if (t == null)
                return;
            dfs(t.l);
            Console.Write(t.key + " ");
            dfs(t.r);
        }
        private void split(Cartesian_item<T> t, T key, ref Cartesian_item<T> l, ref Cartesian_item<T> r)
        {
            if (t == null)
            {
                l = null;
                r = null;
                return;
            }
            else if (key.CompareTo(t.key) == -1)
            {
                split(t.l, key, ref l, ref t.l);
                r = t;
            }
            else
            {
                split(t.r, key, ref t.r, ref r);
                l = t;
            }

            //t.upd_cnt();
            //t.upd_sum();
            t.upd_min();
        }
        private void insert(ref Cartesian_item<T> t, Cartesian_item<T> it)
        {
            if (t == null)
            {
                t = it;
            }
            else
            if (it.prior.CompareTo(t.prior) == 1)
            {
                split(t, it.key, ref it.l, ref it.r);
                t = it;
            }
            else
            {

                if (it.key.CompareTo(t.key) == -1)
                {
                    insert(ref t.l, it);
                }
                else
                {
                    insert(ref t.r, it);
                }
            }

            //t.upd_cnt();
            //t.upd_sum();
            t.upd_min();

        }
        private void merge(ref Cartesian_item<T> t, Cartesian_item<T> l, Cartesian_item<T> r)
        {
            if ((l == null) || (r == null))
            {
                t = (l != null) ? l : r;
                return;
            }
            else if (l.prior.CompareTo(r.prior) == 1)
            {
                merge(ref l.r, l.r, r);
                t = l;
            }
            else
            {
                merge(ref r.l, l, r.l);
                t = r;
            }
            //t.upd_cnt();
            //t.upd_sum();
            t.upd_min();

        }
        private void erase(ref Cartesian_item<T> t, T key)
        {
            if (t.key.CompareTo(key) == 0)
                merge(ref t, t.l, t.r);
            else
            if (key.CompareTo(t.key) == -1)
            {
                erase(ref t.l, key);
            }
            else
            {
                erase(ref t.r, key);
            }
            if (t != null)
            {
                //t.upd_cnt();
                //t.upd_sum();
                t.upd_min();
            }
        }

        private void lower_bound(Cartesian_item<T> t, T key, ref Cartesian_item<T> res, int d = 0, long s = 0)
        {
            if (t.key.CompareTo(key) == 0)
            {
                res = t;
                res.ord = d + 1;
                res.ordsum = s + t.value;
                if (t.l != null)
                {
                    res.ord += t.l.cnt;
                    res.ordsum += t.l.sum;
                }
                return;
            }

            if (t.key.CompareTo(key) == 1)
            {
                res = t;
                res.ord = d + 1;
                res.ordsum = s + t.value;

                if (t.l != null)
                {
                    res.ord += t.l.cnt;
                    res.ordsum += t.l.sum;
                    lower_bound(t.l, key, ref res, d, s);
                }
            }
            else
            {
                d++;
                s += t.value;
                if (t.l != null)
                {
                    d += t.l.cnt;
                    s += t.l.sum;
                }


                if (t.r != null)
                    lower_bound(t.r, key, ref res, d, s);
            }

        }

        private void find_by_order(Cartesian_item<T> t, int K, ref Cartesian_item<T> res, int d = 0, long s = 0)
        {
            int key = d + 1;
            long skey = s + t.value;
            if (t.l != null)
            {
                key += t.l.cnt;
                skey += t.l.sum;
            }

            if (K == key)
            {
                res = t;
                res.ord = key;
                res.ordsum = skey;
                return;
            }

            if (K < key)
            {
                if (t.l != null)
                    find_by_order(t.l, K, ref res, d, s);
            }
            else
            {
                d = key;
                s = skey;
                if (t.r != null)
                    find_by_order(t.r, K, ref res, d, s);
            }

        }


        private void edit(ref Cartesian_item<T> t, T key, long v)
        {
            if (t.key.CompareTo(key) == 0)
                t.value = v;
            else
            if (key.CompareTo(t.key) == -1)
                edit(ref t.l, key, v);
            else
                edit(ref t.r, key, v);
            t.upd_min();
        }

        public void edit(T key, long v)
        {
            edit (ref root, key, v);
        }

        

        

        public void add(T key, long value)
        {
            Cartesian_item<T> node = new Cartesian_item<T>(key, value);
            insert(ref root, node);
        }

        public void erase(T key)
        {
            erase(ref root, key);
        }

        public long sum(T key)
        {
            if (root == null)
                return 0;
            Cartesian_item<T> res = null;
            lower_bound(root, key, ref res);
            if (res == null)
                return root.sum;
            else
                return (res.ordsum - res.value);
        }

        public Cartesian_item<T> lower_bound(T key)
        {
            Cartesian_item<T> res = null;
            lower_bound(root, key, ref res);
            return res;
        }

        public Cartesian_item<T> find_by_order(int K)
        {
            Cartesian_item<T> res = null;
            find_by_order(root, K, ref res);
            return res;
        }

        public long prefMin(T key)
        {
            Cartesian_item<T> lt = null;
            Cartesian_item<T> rt = null;
            split(root, key, ref lt, ref rt);
            long val = 0;
            if (lt != null)
                val = lt.min;

            merge(ref root, lt, rt);
            return val;
        }

        public long sufMin(T key)
        {
            Cartesian_item<T> lt = null;
            Cartesian_item<T> rt = null;
            split(root, key, ref lt, ref rt);
            long val = 0;
            if (rt != null)
                val = rt.min;

            merge(ref root, lt, rt);
            return val;
        }

        public long Min(T l, T r)
        {
            Cartesian_item<T> lt = null;
            Cartesian_item<T> rt = null;
            Cartesian_item<T> lt2 = null;
            Cartesian_item<T> rt2 = null;

            long val = 0;
            //Разбираем
            split(root, l, ref lt, ref rt);
            if (rt != null)
            {
                split(rt, r, ref lt2, ref rt2);
                if (lt2 != null)
                    val = lt2.min;
                merge(ref rt, lt2, rt2);
            }
            merge(ref root, lt, rt);
            return val;
        }
    }




    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
        {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public class Solution
    {
        //https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
        public int[] LongestObstacleCourseAtEachPosition(int[] obstacles)
        {
            int n = obstacles.Length;
            if (n == 0)
                return new int[] { };
            int[] res = new int[n];
            res[0] = 1;
            Cartesian_tree<(int, int)> ctr = new Cartesian_tree<(int, int)>();
            ctr.add((obstacles[0], 0), 1);
            for (int i = 1; i < n; i++)
            {
                (int, int) key = (obstacles[i], i);
                long val = 1 + ctr.prefMin(key);
                res[i] = (int)val;
                ctr.add(key, val);
            }
            return res;
        }

        //https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/

        public int LengthOfLIS(int[] nums)
        {
            int n = nums.Length;
            if (n == 0)
                return 0;
            Cartesian_tree<(int, int)> ctr = new Cartesian_tree<(int, int)>();
            //Cartesian_item<(int, int)> root = new Cartesian_item<(int, int)>((nums[0], 0), 1);
            ctr.add((nums[0], 0), 1);

            for (int i = 1; i < n; i++)
            {
                (int, int) key = (nums[i], -1);
                long val = 1 + ctr.prefMin(key);
                ctr.add((nums[i], i), val);
            }
            int res = (int)ctr.root.min;
            return res;
        }

       

    public void CountSubsequences(int[] nums)
    {
            Cartesian_tree<int> ctr = new Cartesian_tree<int>();
            ctr.add(nums[0], 1);
            int n = nums.Length;
            for (int i = 1; i < n; i++)
            {
                long v = ctr.sum(nums[i]);
                ctr.add(nums[i], v);
            }
            Console.WriteLine(ctr.root.sum);

    }

        //https://leetcode.com/problems/count-number-of-special-subsequences/
        public int CountSpecialSubsequences(int[] nums)
        {
            int mod = 1000000007;
            int n = nums.Length;
            int[,] pref = new int[3, n];

            int res = 0;
            pref[0, 0] = 0;
            pref[1, 0] = 0;
            pref[2, 0] = 0;
            if (nums[0] == 0)
                pref[0, 0] = 1;

            for (int i = 1; i < n; i++)
            {
                int a = nums[i];
                if (a == 0)
                {
                    pref[0, i] = (2 * pref[0, i - 1] + 1) % mod;
                    pref[1, i] = pref[1, i - 1];
                    pref[2, i] = pref[2, i - 1];
                }
                if (a == 1)
                {
                    pref[0, i] = pref[0, i - 1];
                    pref[1, i] = ((2 * pref[1, i - 1]) % mod + pref[0, i - 1]) % mod;
                    pref[2, i] = pref[2, i - 1];
                }
                if (a == 2)
                {
                    pref[0, i] = pref[0, i - 1];
                    pref[1, i] = pref[1, i - 1];
                    pref[2, i] = ((2 * pref[2, i - 1]) % mod + pref[1, i - 1]) % mod;
                    res = pref[2, i];
                }
            }
            return res;
        }


        //https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/
        public long NumberOfWeeks(int[] milestones)
        {
            //milestones.Select((i)=>(long)i).Sum();
            //(long)milestones.Max();

            var a = milestones.Select(i => (long)i).GroupBy((g) => 1).Select(g => new { res = g.Sum(), maxw = g.Max() }).First();
            long res = a.res;
            long maxw = a.maxw;
            res = Math.Min(res, (res - maxw) * 2 + 1);
            return res;

        }
        public int SumOfLeftLeaves(TreeNode root, int child = 0)
        {
            int res = 0;
            if (root == null)
                return 0;
            if (root.left == null && root.right == null && child == -1)
                return root.val;

            res = res + SumOfLeftLeaves(root.left, -1) + SumOfLeftLeaves(root.right, 1);
            return res;
        }

        public string CountAndSay(int n, string a = "1", int d = 1)
        {
            if (n == d)
                return a;

            StringBuilder res = new StringBuilder("");
            char c = a[0];
            int nrep = 1;
            for (int i = 1; i < a.Length; i++)
            {
                if (c != a[i])
                {
                    res.Append(nrep.ToString().Replace(" ", "")).Append(c);
                    c = a[i];
                    nrep = 1;
                }
                else
                {
                    nrep++;
                }
            }
            res.Append(nrep.ToString().Replace(" ", "")).Append(c);
            d++;
            a = res.ToString();
            return CountAndSay(n, a, d);
        }


        public int LeastInterval(char[] tasks, int n)
        {
            int ntask = tasks.Length;
            if (n == 0)
                return ntask;


            Dictionary<char, int> repo = new Dictionary<char, int>();

            foreach (char c in tasks)
            {
                int nchar = 0;
                if (repo.TryGetValue(c, out nchar))
                {
                    nchar++;
                    repo[c] = nchar;
                }
                else
                {
                    repo.Add(c, 1);
                }
            }


            bool[] pos = new bool[ntask];
            int cpos = 0;
            int maxday = 0;
            var vals = repo.Values.Where((i) => i > 1).OrderByDescending((i) => i).Select((i) => i);
            foreach (int nrep in vals)
            {
                //Ищем свободный день
                while (cpos < ntask && pos[cpos])
                {
                    cpos++;
                }

                for (int i = 0; i < nrep; i++)
                {
                    //0 1 2 3 4 5 6 7 8
                    int inx = cpos + i * (n + 1);
                    if (inx < ntask)
                    {
                        pos[cpos] = true;
                    }
                    else
                    {
                        break;
                    }
                }

                int nlast = cpos + (nrep - 1) * (n + 1) + 1;
                maxday = Math.Max(maxday, nlast);

            }
            maxday = Math.Max(maxday, ntask);

            return maxday;
        }
    }
    class Program
    {
        static void LengthOf()
        {
            Solution sol = new Solution();
            int[] a = { 3, 1, 5, 6, 4, 2 };
            int[] res = sol.LongestObstacleCourseAtEachPosition(a);
            foreach (var t in res)
                Console.Write(t + " ");
        }
        static void Subseq()
        {
            Solution sol = new Solution();
            int[] a = { 0, 1, 2, 0, 1, 2 };
            int res = sol.CountSpecialSubsequences(a);
            Console.WriteLine(res);
        }

        static void OfWeeks()
        {
            int[] milestones = { 1, 2, 5 };
            Solution sol = new Solution();
            long res = sol.NumberOfWeeks(milestones);
            Console.WriteLine(res);
        }

        static void Least()
        {
            char[] tasks = { 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G' };
            int n = 2;
            Solution sol = new Solution();
            int res = sol.LeastInterval(tasks, n);
            Console.WriteLine(res);
        }

        static void Say()
        {
            Solution sol = new Solution();
            string s = sol.CountAndSay(30);
            Console.WriteLine(s);
        }

        static void testTree()
        {
            //Cartesian_item<int> root = null;
            Cartesian_tree<int> ctr = new Cartesian_tree<int>();
            for (int i = 1; i <= 20; i++)
            {
                //Cartesian_item<int> node = new Cartesian_item<int>(i * 10, 1);
                //ctr.insert(ref root, node);
                ctr.add(i * 10, 1);
            }
            ctr.edit(20, 10);
            long res;
            
            

            res = ctr.prefMin(25);
            Console.WriteLine(res);

            res = ctr.sufMin(60);
            Console.WriteLine(res);

            res = ctr.Min(10, 90);
            Console.WriteLine(res);
            
            res = ctr.Min(100, 170);
            Console.WriteLine(res);

            res = ctr.sum(35);
            Console.WriteLine(res);

            Console.WriteLine(ctr.root.min);
            Console.WriteLine(ctr.root.sum);
            /*
            ctr.erase(10);
            ctr.erase(30);
            ctr.erase(20);
            ctr.erase(40);
            ctr.erase(50);

            //Console.WriteLine(root.cnt);

            //Cartesian_item<int> res = null;
            //ctr.lower_bound(root, 45, ref res);

            //ctr.find_by_order(root, 3, ref res);
            var res = ctr.find_by_order(3);
            if (res != null)
            {
                Console.WriteLine(res.key);
                Console.WriteLine(res.ord);
                Console.WriteLine(res.ordsum);
            }
            else
            {
                Console.WriteLine("none");
            }
            //ctr.dfs(res);
            */

        }

        static void code597c()
        {
            string s = Console.ReadLine();
            string[] par = s.Split();
            int n = int.Parse(par[0]);
            int k = int.Parse(par[1]);
            k++;
            int[] a = new int[n];
            for (int i = 0; i < n; i++)
            {
                s = Console.ReadLine();
                a[i] = int.Parse(s);
            }
            Cartesian_tree<int>[] ctr = new Cartesian_tree<int>[k];
            for (int i = 0; i < k; i++)
                ctr[i] = new Cartesian_tree<int>();
                
            for (int i = 0; i < n; i++)
            {
                for (int j = k-1; j > 0; j--)
                {
                    long v = ctr[j-1].sum(a[i]);
                    if (v > 0)
                        ctr[j].add(a[i], v);
                }
                ctr[0].add(a[i], 1);
            }
            if (ctr[k-1].root == null)
                Console.WriteLine(0);
            else  
                Console.WriteLine(ctr[k-1].root.sum);
        }

        static void Main(string[] args)
        {
            //https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/
            //https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

            //LengthOf();
            StreamReader reader = new StreamReader("input.txt");
            //StreamWriter writer = new StreamWriter("output.txt");
            Console.SetIn(reader);
            //Console.SetOut(writer);
            code597c();
            //testTree();
        }
    }
}
