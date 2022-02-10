'''CodeForces: A. Book Reading'''

if __name__ == '__main__':
    n, t = map(int, input().split())
    arr = list(map(int, input().split()))
    for i, v in enumerate(arr):
        time_remaining = 86400 - v
        t -= time_remaining
        if t <= 0:
            print(i + 1)
            break
