'''HackerRank: Find Digits'''


def find_digits(n):
    temp = n
    count = 0
    while temp != 0:
        d = temp % 10
        if d != 0 and n % d == 0:
            count += 1
        temp //= 10
    return count


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(find_digits(n))
