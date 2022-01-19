# A standard representation of sparse matrices in sequential languages is to use an array with one element per row each
# of which contains a linked-list of the nonzero values in that row along with their column number.

from numpy import array
from numpy import count_nonzero
from scipy.sparse import csr_matrix

# A =
# 2.0   -1.0    0       0
# -1.0  2.0     -1.0    0
# 0	    -1.0	2.0	    -1.0
# 0	    0	    -1.0	2.0

# A = [[(0, 2.0), (1, -1.0)],
#      [(0, -1.0), (1, 2.0), (2, -1.0)],
#      [(1, -1.0), (2, 2.0), (3, -1.0)],
#      [(2, -1.0), (3, 2.0)]]

# create dense matrix

A = array([[1, 0, 0, 1, 0, 0], [0, 0, 2, 0, 0, 1], [0, 0, 0, 2, 0, 0]])
print(A)

# convert to sparse matrix (CSR method)
S = csr_matrix(A)
print(S)

# reconstruct dense matrix
B = S.todense()
print(B)

