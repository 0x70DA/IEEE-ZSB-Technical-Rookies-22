def main():
    num = input()
    counter = 0
    while True:
        while len(num) < 4:
            num += '0'
        counter += 1
        ascen = ''.join(sorted(list(num)))
        descen = ''.join(sorted(list(num), reverse=True))
        num = str(int(descen) - int(ascen))
        if num == '6174':
            break
        else:
            continue

    print(counter)


if __name__ == '__main__':
    main()
