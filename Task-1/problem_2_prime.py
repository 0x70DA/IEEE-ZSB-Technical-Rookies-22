"""Print all prime numbers from 1 to n inclusive."""


def main():
    n = int(input())
    if n >= 2:
        primes = [2]  # 2 is the only even prime number.
        # Only check for odd numbers.
        for i in range(3, n+1, 2):
            for j in range(3, i, 2):
                if i % j == 0:
                    break
            else:
                primes.append(i)
        print(*primes)


if __name__ == '__main__':
    main()
