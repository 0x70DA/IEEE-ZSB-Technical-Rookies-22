"""Given a sorted list, remove duplicate elements."""


def main():
    arr = set(map(int, input().split(' ')))
    print(*arr)


if __name__ == '__main__':
    main()
