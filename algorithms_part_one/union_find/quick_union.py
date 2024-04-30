"""Python implementation of Quick Union."""

class QuickUnion:
    """It's a tree structure."""
    def __init__(self, n: int):
        """Each value of array is root of the element(node)."""
        self.array = list(range(n))
    
    
    def _find_root(self, p: int) -> int:
        """Find the root node of given element."""
        # this means p is root
        if self.array[p] == p:
            return p
        return self._find_root(self.array[p])
    
        #### Another solution ####
        # while self.array[p] != p:
        #     p = self.array[p]
        # return p
    
        
    def union(self, p: int, q: int) -> None:
        """Lazy approach.
        We only need to change one item per union operation.
        First item becomes child of second item.
        
        n=10
        union(3,4) -> [0, 1, 2, 4, 4, 5, 6, 7, 8, 9]
        union(3,8) -> [0, 1, 2, 4, 8, 5, 6, 7, 8, 9] 
        union(2,8) -> [0, 1, 8, 4, 8, 5, 6, 7, 8, 9]
        union(0,1) -> [1, 1, 8, 4, 8, 5, 6, 7, 8, 9]
        union(0,4) -> [1, 8, 8, 4, 8, 5, 6, 7, 8, 9]
        
        """
        # 1. find the root of first item
        root_p = self._find_root(p)
        root_q = self._find_root(q)
        
        # 2. Make the root of the first item a child of root of second item
        self.array[root_p] = root_q
    
    def connected(self, p: int, q: int) -> bool:
        """
        """
        root_p = self._find_root(p)
        root_q = self._find_root(q)
        return root_p == root_q


if __name__ == "__main__":
    qu = QuickUnion(10)
    print("Before", qu.array)
    qu.union(3,4)
    qu.union(3,8)
    qu.union(2,8)
    qu.union(0,1)
    qu.union(0,4)
    print("After", qu.array)
    print(qu.connected(0,8)) # True
    print(qu.connected(3,1)) # True
    print(qu.connected(0,9)) # False


# 06:58 QUICK-UNION IS ALSO TOO SLOW
#
# COST MODEL. Number of array accesses (for read or write).
# algorithm   init union find
# quick-find    N    N    1
# quick-union   N    N*   N <- worst case, if tree is tall
#     * Included cost of finding roots

# QUICK-FIND  DEFECT.  Too slow for huge problems
#   * UNION too expensive (N array accesses)
#   * Trees are flat, but too expensive to keep them flat.
#
# QUICK-UNION DEFECT.
#   * Trees can get too tall.
#   * FIND too expensive (could be N array accesses).
#


#  """ Quick-union [lazy approach].
#
#      Uses a rooted tree.  Each element is in a rooted tree.
#      Each item can be associated with a root.
#  """
# --------------------------------------------------------------
# Lecture Week 1 "Quick Union"(7:50)
# --------------------------------------------------------------
# 00:32 QUICK-UNION [Lazy approach; Avoid doing work until we are force to]
# DATA STRUCTURE
# * Integer array id[] of size N.
#   Array represents a set of trees, called a forest.
# * Interpretation: id[i] is parent of i.
# * Root of i is id[id[id[...id[i]...]]].
#   ... => Keep going until id doesn't change (algorithm ensures no cycles)
#
#  i   0 1 2 3 4 5 6 7 8 9
# id[] 0 1 9 4 9 6 6 7 8 9
#
# 0 1 9   6 8 8
#    / \  |
#   2   4 5
#       |
#       3
#
# Ex: id[2]=9 -> 9 is parent of 2
# Ex: id[4]=9 -> 9 is parent of 4
# Ex: id[3]=4 -> 4 is parent of 3
# Ex: id[5]=6 -> 6 is parent of 5
#
# Root of 3 is id[id[3]]
#              id[  4  ]
#                   9

# 01:43 QUESTION: Suppose that in a quick-union data structure on 10 elements
# that the id[] array is
#   0 9 6 5 4 2 6 1 0 5
#   0 1 2 3 4 5 6 7 8 9
# What are the roots of 3 and 7?
# ANSWER: 6 and 6
#
#  i   0 1 2 3 4 5 6 7 8 9
# id[] 0 9 6 5 4 2 6 1 0 5
#
#  0    4    6
#  |         |
#  8         2
#            |
#            5
#           / \
#          3   9
#              |
#              1
#              |
#              7
#

# 2:42
# FIND. Check if p and q have the same root.
#
# UNION. To merge components containing p and q, set the id of
# p's root to the id of q's root.
#
#  i   0 1 2 3 4 5 6 7 8 9
# id[] 0 1 9 4 9 6 6 7 8 9
#
# 0  1  9   6  7  8
#      / \  |
#     2   4 5=q
#         |
#         3=p
#
#
#  i   0 1 2 3 4 5 6 7 8 9
# id[] 0 1 9 4 9 6 6 7 8 6
#      . . . . . . . . . X <- Only one value changes
#
# 0  1     6  7  8
#         /|
#        9 5=q
#       / \
#      2   4
#          |
#          3=p
#
# -----------------------------
#        i   0 1 2 3 4 5 6 7 8 9
#  INI: id[] 0 1 2 3 4 5 6 7 8 9
#
# 0  1  2  3  4  5  6  7  8  9
#
#  03:21 -- union(4, 3) --------
#  WAS: id[] 0 1 2 3 4 5 6 7 8 9
#  NOW: id[] 0 1 2 3 3 5 6 7 8 9
#            . . . . X . . . . .
#
# 0  1  2  3     5  6  7  8  9
#          |
#          4
#
#  03:37 -- union(3, 8) --------
#  WAS: id[] 0 1 2 3 3 5 6 7 8 9
#  NOW: id[] 0 1 2 8 3 5 6 7 8 9
#            . . . X . . . . . .
#
# 0  1  2        5  6  7  8  9
#                         |
#                         3
#                         |
#                         4
#
#  03:51 -- union(6, 5) --------
#  WAS: id[] 0 1 2 8 3 5 6 7 8 9
#  NOW: id[] 0 1 2 8 3 5 5 7 8 9
#            . . . . . . X . . .
#
# 0  1  2        5     7  8  9
#                |        |
#                6        3
#                         |
#                         4
#
#  03:55 -- union(9, 4) --------
#  WAS: id[] 0 1 2 8 3 5 5 7 8 9
#  NOW: id[] 0 1 2 8 3 5 5 7 8 8
#            . . . . . . . . . X
#
# 0  1  2        5     7  8
#                |        |\
#                6        3 9
#                         |
#                         4
#
#
#  04:12 -- union(2, 1) --------
#  WAS: id[] 0 1 2 8 3 5 5 7 8 8
#  NOW: id[] 0 1 1 8 3 5 5 7 8 8
#            . . X . . . . . . .
#
# 0  1           5     7  8
#    |           |        |\
#    2           6        3 9
#                         |
#                         4
#
#  04:12 -- union(5, 0) --------
#  WAS: id[] 0 1 1 8 3 5 5 7 8 8
#  NOW: id[] 0 1 1 8 3 0 5 7 8 8
#            . . . . . X . . . .
#
# 0  1                 7  8
# |  |                    |\
# 5  2                    3 9
# |                       |
# 6                       4
#
#
#  04:42 -- union(7, 2) --------
#  WAS: id[] 0 1 1 8 3 0 5 7 8 8
#  NOW: id[] 0 1 1 8 3 0 5 1 8 8
#            . . . . . . . X . .
#
# 0  1                    8
# |  |\                   |\
# 5  2 7                  3 9
# |                       |
# 6                       4
#
#
#  04:48 -- union(6, 1) --------
#  WAS: id[] 0 1 1 8 3 0 5 1 8 8
#  NOW: id[] 1 1 1 8 3 0 5 1 8 8
#            X . . . . . . . . .
#
#   1                    8
#  /|\                   |\
# 0 2 7                  3 9
# |                      |
# 5                      4
# |
# 6
#
#
#
#  05:08 -- union(7, 3) --------
#  WAS: id[] 1 1 1 8 3 0 5 1 8 8
#  NOW: id[] 1 8 1 8 3 0 5 1 8 8
#            . X . . . . . . . .
#
#          -8
#         / |\
#     1--+  3 9
#    /|\    |
#   0 2 7   4
#   |
#   5
#   |
#   6


# 07:43 QUESTION: What is the maximum number of array accesses during a
# find operation when using the quick-union stata structure on N elements?
# ANSWER: linear
