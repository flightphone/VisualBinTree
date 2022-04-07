# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class VisualBinTree:
    def __init__(self):
        self.vertexes = ""
        self.edges = ""

    
    def dfs_dot(self, nd, num):
        if nd is None:
            self.vertexes += f"{num} [label = \"null\"]\n"
            return

        self.vertexes += f"{num} [label = \"{nd.val}\"]\n"
        
        if ((nd.left is not None) or (nd.right is not None)):
            self.edges += f"{num} -- {2*num}\n"
            self.dfs_dot(nd.left, 2*num)
            self.edges += f"{num} -- {2*num + 1}\n"
            self.dfs_dot(nd.right, 2*num + 1)
        
        return

    # Return string dot format. 
    # For print graph input return string in https://edotor.net/
    def dotBinTree(self, node):
        self.vertexes = ""
        self.edges = ""
        self.dfs_dot(node, 1)
        result = "graph  { \n" + self.vertexes + self.edges + "}"
        return result

    # Creating tree from array
    def createBinTree(self, a):
        nn = len(a)
        root = TreeNode(a[0])
        level = [root]
        start = 1
        d = 2 * len(level)
        while start < nn:
            level2 = [] 
            c = 0
            for i in range(start, min(start+d, nn)):
                nod = TreeNode(a[i])
                if (((i - start) % 2 == 0) and (a[i] is not None)):
                    level[c].left = nod

                if ((i - start) % 2 == 1):
                    if (a[i] is not None):
                        level[c].right = nod
                    c += 1

                if (a[i] is not None):
                    level2.append(nod)

            level.clear()
            for t in level2:
                level.append(t)

            start += d
            d = 2 * len(level)

        return root



def main():
    null = None
    a = [0, 2, 4, 1, null, 3, -1, 5, 1, null, 6, null, 8]

    vb = VisualBinTree()

    # Creating tree from array
    node_tree = vb.createBinTree(a)

    # Return string dot format from tree. 
    # For print graph input return string in https://edotor.net/
    tree_dot = vb.dotBinTree(node_tree)
    print(tree_dot)

if __name__ == '__main__':
    main()

