"""Taken a string, output each word on a line in a rectangular frame."""


def main():
    words = input().split(' ')
    # Find the length of the longest word.
    longest_len = 0
    for word in words:
        if len(word) > longest_len:
            longest_len = len(word)
    longest_len += 4
    print('*' * longest_len)
    for word in words:
        print('* ' + word + ' ' * (longest_len - len(word) - 3) + '*')
    print('*' * longest_len)


if __name__ == '__main__':
    main()
