"""Check if a given word is a palindrome."""


def main():
    word = input()
    if word == word[::-1]:
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    main()

# Another way would be to push the characters to a stack and then pop them, effectively reversing the word, then check if it equals the original word.
