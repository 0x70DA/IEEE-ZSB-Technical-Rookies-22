def pageCount(n, p):
    arr = [(0, 1)]
    for i in range(2, n + 1, 2):
        arr.append((i, i + 1))
    for i, row in enumerate(arr):
        if p in row:
            ind = i
    print(ind if ind < (len(arr) - 1 - ind) else (len(arr) - 1 - ind))


if __name__ == '__main__':
    n = int(input())
    p = int(input())
    pageCount(n, p)
