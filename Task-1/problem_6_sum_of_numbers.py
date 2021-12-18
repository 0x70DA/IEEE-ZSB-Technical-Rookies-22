"""Find the sum of numbers from 1 to n inclusive."""

def find_sum(n):
    if n == 1:
        return n
    return n + find_sum(n - 1)

def main():
    n = int(input())
    print(find_sum(n))


if __name__ == '__main__':
    main()