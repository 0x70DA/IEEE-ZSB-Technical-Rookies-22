'''HackerRank: Circular Array Rotation'''


if __name__ == '__main__':
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(q):
        i = int(input())
        print(arr[(i + n - k) % n])
