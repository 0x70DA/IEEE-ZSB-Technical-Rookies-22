"""Given a numbuer n, print the first n numbers of the fibonacci sequence."""


def fib_sequence(n):
    if n == 1:
        print(0)
    elif n > 1:
        num = 0
        next_num = 1
        print(num, next_num, sep=' ', end=' ')
        for _ in range(n - 2):
            num, next_num = next_num, next_num + num
            print(next_num, end=' ')


def main():
    n = int(input())
    fib_sequence(n)


if __name__ == '__main__':
    main()
