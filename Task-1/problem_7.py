"""Find the sum of multiples of three or five from 1 to n inclusive."""


def find_sum(n):
    nums_sum = 0
    for i in range(3, n+1):
        if i % 3 == 0 or i % 5 == 0:
            nums_sum += i
    return nums_sum


def main():
    n = int(input())
    print(find_sum(n))


if __name__ == '__main__':
    main()
