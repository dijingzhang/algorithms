class SparseMatrix():
    def __init__(self, matrix):
        self.idx_val = collections.defaultdict(dict)
        self.w, self.h = len(matrix[0]), len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    self.idx_val[i][j] = matrix[i][j]

    def get(self, i, j):
        if i in self.idx_val and j in self.idx_val[i]:
            return self.idx_val[i][j]
        return 0

    def set(self, i, j, val):
        if val == 0:
            del self.idx_val[i][j]
        else:
            self.idx_val[i][j] = val
        return

    def add(self, new_matrix):
        for row_idx, sub_dict in new_matrix.idx_val.items():
            for col_idx, val in sub_dict.items():
                if row_idx in self.idx_val and col_idx in self.idx_val[row_idx]:
                    self.set(row_idx, col_idx, val + self.get(row_idx, col_idx))
                else:
                    self.set(row_idx, col_idx, val)
        return

    def multiply(self, new_matrix):
        if self.w != new_matrix.h:
            return [[]]
        m = [[0] * new_matrix.w for _ in range(self.h)]
        for i in range(len(m)):
            for j in range(len(m[0])):
                tmp = 0
                for k in range(self.w):
                    if i in self.idx_val and k in self.idx_val[i] and k in new_matrix.idx_val and j in new_matrix.idx_val[k]:
                        tmp += self.idx_val[i][k] * new_matrix.idx_val[k][j]
                m[i][j] = tmp
        return m
