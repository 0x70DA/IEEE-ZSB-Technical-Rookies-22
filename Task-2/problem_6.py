"""Find second max number in a list."""


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    max_num = max(arr)
    while max(arr) == max_num:
        arr.remove(max(arr))
    print(max(arr))


if __name__ == '__main__':
    main()
