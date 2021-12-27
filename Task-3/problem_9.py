def countingValleys(path):
    count = 0
    s = [0]
    for i in path:
        s.append(s[-1] + 1 if i == 'U' else s[-1] - 1)
    for i in range(1, len(s)):
        if s[i] == 0 and s[i - 1] == -1:
            count += 1
    print(count)


if __name__ == '__main__':
    steps = int(input())
    path = list(input())
    countingValleys(path)
