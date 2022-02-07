"""Find the number of r's in the first n letters of an infinte sequence."""


def main():
    seq, n = input(), int(input())
    seq = seq * (n // len(seq)) + seq[0:(n % len(seq))]
    print(seq.count('r'))


if __name__ == '__main__':
    main()
