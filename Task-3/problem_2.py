def getTotalX(a, b):
    count = 0
    for i in range(1, 101):
        if all(i % n == 0 for n in a) and all(m % i == 0 for m in b):
            count += 1
    return count


def main():
    n, m = map(int, input().split)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(getTotalX(a, b))


if __name__ == '__main__':
    main()
