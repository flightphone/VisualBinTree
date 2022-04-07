	# Creating and print tree from array
	
	null = None
    a = [0, 2, 4, 1, null, 3, -1, 5, 1, null, 6, null, 8]

    vb = VisualBinTree()

    # Creating tree from array
    node_tree = vb.createBinTree(a)

    # Return string dot format from tree. 
    # For print graph input return string in https://edotor.net/
    tree_dot = vb.dotBinTree(node_tree)
    print(tree_dot)