"""Given a square matrix, output the absolute difference of the sums of the two diagonals."""


def diagonal_difference(arr, n):
    primary = sum([arr[i][i] for i in range(n)])
    secondary = sum([arr[i][n - 1 - i] for i in range(n)])
    return abs(primary - secondary)


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append([i for i in list(map(int, input().split()))])
    print(diagonal_difference(arr, n))


if __name__ == '__main__':
    main()
