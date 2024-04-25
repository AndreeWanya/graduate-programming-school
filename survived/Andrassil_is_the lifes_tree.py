def tree_converting(tree: list, encr: bool) -> list:
    another_tree = []
    if encr:
        for s in tree:
            s = list(s)
            for i in range(len(s)):
                if s[i] == '.':
                    s[i] = 0
                else:
                    s[i] = 1
            another_tree.append(s)
    else:
        for s in tree:
            for i in range(len(s)):
                if s[i] == 0:
                    s[i] = '.'
                else:
                    s[i] = '+'
            another_tree.append(''.join(s))
    return another_tree
def TreeOfLife(H: int, W: int, N: int, tree: list) -> list:
    tree = tree_converting(tree, True)
    for i in range(N):
        for h in range(H):
            for w in range(W):
                tree[h][w] += 1
        if i % 2 != 0:
            del_matrix = [[1 for x in range (W+2)] for y in range(H+2)]
            for h in range(H):
                for w in range(W):
                    if tree[h][w] >= 3:
                        del_matrix[h - 1][w] = 0
                        del_matrix[h + 1][w] = 0
                        del_matrix[h][w] = 0
                        del_matrix[h][w -1] = 0
                        del_matrix[h][w + 1] = 0
            for h in range(H):
                for w in range(W):
                    if del_matrix[h][w] == 0:
                        tree[h][w] = 0
    tree = tree_converting(tree, False)
    return tree


#print(TreeOfLife(3, 4, 12, ['.+..', '..+.', '.+..']))