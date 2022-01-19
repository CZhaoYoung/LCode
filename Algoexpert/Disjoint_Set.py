# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        # setting the root of y as the root of x,
        # which means x and y ara in the same union
        if rootx != rooty:
            for i in range(len(self.root)):
                print(i)
                if self.root[i] == rooty:
                    self.root[i] = rootx

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test
uf = UnionFind(10)

# 1-2-4-5 3-8-7 6-9
# uf.union(1, 2)
# uf.union(2, 4)
# uf.union(4, 5)
# uf.union(3, 8)
# uf.union(8, 7)
# uf.union(6, 9)
#
# print(uf.connected(1, 5))
# print(uf.connected(5, 7))
# print(uf.connected(4, 9))
