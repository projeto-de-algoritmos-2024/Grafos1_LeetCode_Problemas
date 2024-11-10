from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        if not matrix[0]:
            return 0
        
        r, c = len(matrix), len(matrix[0])
        
        distance = [[0] * c for _ in range(r)]
        
        def DFS(x, y):
            if distance[x][y] != 0:
                return distance[x][y]
            max_path = 1
            
            left = x > 0 and matrix[x][y] < matrix[x - 1][y]
            right = x < r - 1 and matrix[x][y] < matrix[x + 1][y]
            bot = y > 0 and matrix[x][y] < matrix[x][y - 1]
            top = y < c - 1 and matrix[x][y] < matrix[x][y + 1]

            if left:
                max_path = max(max_path, 1 + DFS(x - 1, y))
            
            if right:
                max_path = max(max_path, 1 + DFS(x + 1, y))
            
            if bot:
                max_path = max(max_path, 1 + DFS(x, y - 1))
            
            if top:
                max_path = max(max_path, 1 + DFS(x, y + 1))
            
            distance[x][y] = max_path
            return max_path
        
        path = 0
        for i in range(r):
            for j in range(c):
                path = max(path, DFS(i, j))
        
        return path
