'''HackerRank: Modified Kaprekar Numbers'''


def kaprekar(n):
    d = len(str(n))
    sq = str(n ** 2)
    if len(sq) % 2 == 0:
        l = sq[0:d]
        r = sq[d:]
    else:
        l = sq[0:d-1]
        r = sq[d-1:]
    l = int(l) if l != '' else 0
    r = int(r) if r != '' else 0
    if r + l == n:
        print(n, end=' ')
        return True


if __name__ == '__main__':
    p, q = int(input()), int(input())
    found_kaprekar = False
    for n in range(p, q+1):
        if kaprekar(n):
            found_kaprekar = True
    if not found_kaprekar:
        print('INVALID RANGE')


# Another solution.

# def kaprekar(p, q):
#     res = []
#     for n in range(p, q+1):
#         d = len(str(n))
#         n2 = str(n ** 2)
#         r = n2[-1:-(d+1):-1]
#         l = n2[-(d+1)::-1]
#         r = int(r[::-1]) if r != '' else 0
#         l = int(l[::-1]) if l != '' else 0
#         if l + r == n:
#             res.append(n)
#     return res


# if __name__ == '__main__':
#     p, q = int(input()), int(input())
#     res = kaprekar(p, q)
#     if res == []:
#         print('INVALID RANGE')
#     else:
#         print(*res)
