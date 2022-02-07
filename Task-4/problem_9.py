'''HackerRank: Cavity Map'''


def cavity_map(grid, n):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for r in range(1, n - 1):
        for c in range(1, n - 1):
            if all([grid[r][c] > grid[r+i][c+j] for i, j in directions]):
                grid[r][c] = 'X'
    return grid


if __name__ == '__main__':
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    result = cavity_map(grid, n)
    for row in result:
        print(''.join(map(str, row)))
