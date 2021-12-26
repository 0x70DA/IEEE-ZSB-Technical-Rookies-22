"""Given a sorted list, remove duplicate elements."""


def main():
    arr = list(map(int, input().split(' ')))
    distinct = [arr[0]]
    i = 0
    for j in range(1, len(arr)):
        if arr[j] == distinct[i]:
            continue
        distinct.append(arr[j])
        i += 1
    print(*distinct)



if __name__ == '__main__':
    main()
