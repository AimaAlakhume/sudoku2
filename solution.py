def solution(grid):
        
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        squares = [[set() for i in range(3)] for j in range(3)]
        
        for i in range(9):
            for j in range(9):
                value = grid[i][j]
                if value == ".":
                    continue
                if value in rows[i] or value in columns[j] or value in squares[i//3][j//3]:
                    return False

                rows[i].add(value)
                columns[j].add(value)
                squares[i//3][j//3].add(value)
        
        return True
