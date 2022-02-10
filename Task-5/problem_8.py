'''HackerEarth: Bob and String'''


def anagram(s1, s2):
    ops = 0
    d1, d2 = {}, {}
    for c in s1:
        try:
            d1[c] += 1
        except KeyError:
            d1[c] = 1

    for c in s2:
        try:
            d2[c] += 1
        except KeyError:
            d2[c] = 1

    for k, v in d2.items():
        if k not in d1.keys():
            ops += v
        elif d1[k] != v:
            ops += abs(d1[k] - v)

    for k, v in d1.items():
        if k not in d2.keys():
            ops += v

    print(ops)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        anagram(input(), input())
