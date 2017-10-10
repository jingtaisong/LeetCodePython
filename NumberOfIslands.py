from unittest import (TestCase, main)

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])
        if n == 0:
            return 0

        labelGrid = [[0] * n for _ in range(0, m)]

        q = list()  # python list can be used as a stack!
        numberOfIslands = 0

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '0':
                    continue

                if labelGrid[i][j] != 0:
                    continue  # means it has been visited

                # a new island found!
                numberOfIslands += 1
                q.append((i, j))
                while len(q):
                    current_i, current_j = q.pop()
                    labelGrid[current_i][current_j] = numberOfIslands

                    if current_j < n - 1:
                        new_i = current_i
                        new_j = current_j + 1
                        if grid[new_i][new_j] == '1' and labelGrid[new_i][new_j] == 0:
                            q.append((new_i, new_j))

                    if current_i < m - 1:
                        new_i = current_i + 1
                        new_j = current_j
                        if grid[new_i][new_j] == '1' and labelGrid[new_i][new_j] == 0:
                            q.append((new_i, new_j))

                    if current_j > 0:
                        new_i = current_i
                        new_j = current_j - 1
                        if grid[new_i][new_j] == '1' and labelGrid[new_i][new_j] == 0:
                            q.append((new_i, new_j))

                    if current_i > 0:
                        new_i = current_i - 1
                        new_j = current_j
                        if grid[new_i][new_j] == '1' and labelGrid[new_i][new_j] == 0:
                            q.append((new_i, new_j))

        return numberOfIslands

class TestNumberOfIslands(TestCase):
    """
    Regtest
    """
    def setUp(self):
        self.test_object = [
{
    'test_grid': [],
    'test_output': 0
}, {
    'test_grid': [[]],
    'test_output': 0
}, {
    'test_grid': ['1'],
    'test_output': 1
}, {
    'test_grid': ['11'],
    'test_output': 1
}, {
    'test_grid': ['101'],
    'test_output': 2
}, {
    'test_grid': ['1','0','1'],
    'test_output': 2
}, {
    'test_grid': ['10','11'],
    'test_output': 1
}, {
    'test_grid': ['101','010'],
    'test_output': 3
}, {
    'test_grid': ["11110","11010","11000","00000"],
    'test_output': 1
}, {
    'test_grid': ["11000","11000","00100","00011"],
    'test_output': 3
}, {
    'test_grid': ["1111111","0000001","1111101","1000101","1010101","1011101","1111111"],
    'test_output': 1
}
        ]

    def test_result(self):
        obj = Solution()

        for test_case in self.test_object:
            grid = test_case['test_grid']
            answer = obj.numIslands(grid)

            self.assertEqual(answer, test_case['test_output'])

if __name__ == '__main__':
    main()