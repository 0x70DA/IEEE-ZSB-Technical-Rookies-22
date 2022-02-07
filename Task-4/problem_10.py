'''HackerRank: Electronics Shop'''


def get_money_spent(c, keyboards, drives):
    max_spent = -1
    for i in keyboards:
        for j in drives:
            cost = i + j
            if cost > max_spent and cost <= b:
                max_spent = cost
    return max_spent


if __name__ == '__main__':
    b, n, m = map(int, input().split())
    keyboards = list(map(int, input().split()))
    drives = list(map(int, input().split()))
    print(get_money_spent(b, keyboards, drives))

# Another solution.

# def get_money_spent(c, keyboards, drives):
#     keyboards.sort(reverse=True)
#     drives.sort()
#     max_spent = -1
#     for i in keyboards:
#         for j in drives:
#             cost = i + j
#             if cost > b:
#                 break
#             if cost > max_spent:
#                 max_spent = cost
#     return max_spent
