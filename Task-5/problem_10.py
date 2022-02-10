'''HackerRank: HackerRank in a String!'''


def hackerrank_in_string(s):
    h = 'hackerrank'
    if len(s) < len(h):
        print('NO')
        return
    
    i = 0
    for c in s:
        if i >= len(h):
            break
        if c == h[i]:
            i += 1

    print('YES') if i >= len(h) else print('NO')


if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        hackerrank_in_string(s)
