def kangaroo(x1, v1, x2, v2):
    if (x1 > x2 and v2 <= v1) or (x2 > x1 and v1 <= v2) or (v1 == v2):
        print("NO")
        return
    while True:
        x1 += v1
        x2 += v2
        if x1 == x2:
            print("YES")
            return
        elif x1 > x2:
            print("NO")
            return


if __name__ == '__main__':
    x1, v1, x2, v2 = map(int, input().split())
    kangaroo(x1, v1, x2, v2)
