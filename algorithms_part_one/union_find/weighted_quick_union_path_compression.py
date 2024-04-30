"""Python implementation of Weighted Quick Union with path compression."""

class WeightedQuickUnionPathCompression:
    """We have to keep track of the size of each tree."""
    def __init__(self, n: int):
        self.array = list(range(n))
        self.size_array = [1] * n
        
    
    def _find_root(self, p: int) -> int:
        if self.array[p] == p:
            return p
        return self._find_root(self.array[p])

        # ### path comprehension with one line added
        # while self.array[p] != p:
        #     self.array[p] = self.array[self.array[p]]
        #     p = self.array[p]
        # return p
        

    def union(self, p: int, q: int) -> None:
        """Always place smaller tree as a child of root node.
        Also update the element of array to root node to flatten out the tree.
        
        Naive Quick Union implementation always chose 2nd element as root node.
        Weighted implementation ensures bigger tree becomes root node.
        This avoids tall tree issue.

        e.g.
        n=10
        union(3,4) -> [0, 1, 2, 4, 4, 5, 6, 7, 8, 9]
        union(3,8) -> [0, 1, 2, 4, 4, 5, 6, 7, 4, 9] 
        union(2,8) -> [0, 1, 4, 4, 4, 5, 6, 7, 4, 9]
        union(0,1) -> [1, 1, 8, 4, 4, 5, 6, 7, 4, 9]
        union(0,4) -> [1, 4, 4, 4, 4, 5, 6, 7, 4, 9]
        """
        root_p = self._find_root(p)
        root_q = self._find_root(q)
        
        # path compression
        self.array[p] = root_p
        self.array[q] = root_q
        
        size_p = self.size_array[root_p]
        size_q = self.size_array[root_q]
        
        # 1. check size of each tree
        if size_p > size_q:
            smaller_tree = root_q
            bigger_tree = root_p
        else:
            smaller_tree = root_p
            bigger_tree = root_q
        
        self.array[smaller_tree] = bigger_tree
        
        # 2. only update the size of tree of root node
        self.size_array[bigger_tree] += self.size_array[smaller_tree]

    
    def connected(self, p: int, q: int) -> bool:
        return self._find_root(p) == self._find_root(q)
        
        
if __name__ == "__main__":
    wqupc = WeightedQuickUnionPathCompression(10)
    # print("Before", wqupc.array)
    # wqupc.union(3,4)
    # wqupc.union(3,8)
    # wqupc.union(2,8)
    # wqupc.union(0,1)
    # wqupc.union(0,4)
    # print("After", wqupc.array)
    # assert wqupc.connected(0,8) == True
    # assert wqupc.connected(3,1) == True
    # assert wqupc.connected(0,9) == False
    
    wqupc.union(4, 3)       
    wqupc.union(3, 8)                
    wqupc.union(6, 5)       
    wqupc.union(9, 4)
    wqupc.union(2, 1)
    wqupc.union(5, 0)
    wqupc.union(7, 2)
    wqupc.union(6, 1)
    wqupc.union(7, 3)
    assert wqupc.array == [5, 1, 1, 1, 3, 1, 5, 1, 3, 3], f"array is {wqupc.array}"
    # """
    #         1
    #     /  | \   \
    #    2   3  5   7
    #     / / |  | \
    #    9 8  4  0  6
    # """
    assert wqupc.connected(0, 7) == True
    assert wqupc.connected(8, 9) == True