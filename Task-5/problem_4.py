'''HackerRank: Beautiful Triplets'''


def beautiful_triplets(arr, d, n):
    count = 0
    for i in arr:
        if i+d in arr and i + 2*d in arr:
            count += 1
    return count


if __name__ == '__main__':
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    print(beautiful_triplets(arr, d, n))


# Another solution.
# def beautiful_triplets(arr, d, n):
#     count = 0
#     for i in range(n - 2):
#         c = arr[i] + d
#         x = False
#         for j in range(i + 1, n):
#             if arr[j] == c:
#                 if x == True:
#                     count += 1
#                     break
#                 c += d
#                 x = True
#             elif arr[j] > c:
#                 break
#     return count
