"""Find the minimum distance between 2 similar numbers in a list"""
import math


def main():
    arr = list(map(int, input().split()))
    min_distance = math.inf
    for i in range(len(arr)):
        j = 1
        while j < min_distance and i + j < len(arr) - 1:
            if arr[i] == arr[i+j]:
                min_distance = j
                break
            j += 1
    print(min_distance)


if __name__ == '__main__':
    main()
