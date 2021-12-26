"""Find the minimum distance between two similar elements in a list."""
import math


def main():
    arr = list(map(int, input().split()))
    min_distance = math.inf  # Initially set to a very large number.
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                min_distance = min(min_distance, j - i)
                break
    print(min_distance)


if __name__ == '__main__':
    main()
