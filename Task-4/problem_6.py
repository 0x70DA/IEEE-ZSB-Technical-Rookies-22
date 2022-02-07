'''HackerRank: Chocolate Feast'''


def chocolate_feast(n, c, m):
    eaten = wrappers = n // c
    while not wrappers < m:
        exchanged = wrappers // m
        eaten += exchanged
        wrappers = exchanged + wrappers % m
    return eaten


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, c, m = map(int, input().split())
        print(chocolate_feast(n, c, m))
