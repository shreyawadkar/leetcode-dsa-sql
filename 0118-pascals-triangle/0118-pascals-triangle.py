class Solution(object):
    def generate(self, numRows):
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)  # Start with all 1s
            for j in range(1, i):
                # Each value is the sum of the two values above it
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)

        return triangle
        