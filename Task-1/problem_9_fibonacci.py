"""Given a numbuer n, print the first n numbers of the fibonacci sequence."""


def fib_sequence(n):
    if n == 1:
        return 0
    arr = [0, 1]
    for _ in range(n - 2):
        # Append the sum of the last two numbers.
        arr.append(arr[-1] + arr[-2])
    return arr


def main():
    n = int(input())
    print(*fib_sequence(n))


if __name__ == '__main__':
    main()
