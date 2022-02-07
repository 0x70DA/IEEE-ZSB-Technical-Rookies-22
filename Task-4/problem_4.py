
def library_fine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y2 < y1:
        return 10000
    elif y1 == y2 and m2 < m1:
        return 500 * (m1 - m2)
    elif y1 == y2 and m1 == m2 and d2 < d1:
        return 15 * (d1 - d2)
    return 0


if __name__ == '__main__':
    d1, m1, y1 = map(int, input().split())
    d2, m2, y2 = map(int, input().split())
    print(library_fine(d1, m1, y1, d2, m2, y2))
