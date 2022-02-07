'''HackerRank: Manasa and Stones'''


def stones(n, a, b):
    result = []
    i = 0
    j = n - 1
    while i <= n-1 and j >= 0:
        c = a * i + b * j
        if c not in result:
            result.append(c)
        i += 1
        j -= 1
    return result


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = int(input())
        b = int(input())
        result = stones(n, a, b)
        print(' '.join(map(str, sorted(result))))
