if __name__ == '__main__':
    # Get a nested list of names and scores.
    arr = [[input(), float(input())] for _ in range(int(input()))]
    scores = [score for name, score in arr]
    second_lowest = sorted(list(set(scores)))[1]
    names = [name for name, score in arr if score == second_lowest]
    names.sort()
    print(*names, sep='\n')


# Another solution using a dictionary inseted of a nested list.
# d = {}
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     if score in d.keys():
#         d[score].append(name)
#     else:
#         d[score] = [name]
# scores = d.keys()
# second_lowest = sorted(list(set(scores)))[1]
# names = d[second_lowest]
# names.sort()
# print(*names, sep='\n')
