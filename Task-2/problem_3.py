import random


def main():
    # num = str(random.randint(100, 999))
    num = list(str(223))
    tries = 0
    while True:
        tries += 1
        guess = list(input("Guess a 3-digit number: "))
        # Make sure that the input is valid.
        if len(guess) != 3:
            continue
        if guess == num:
            print(f"That's right! You got it in {tries} tries.")
            break

        hit = 0
        miss = 0
        num_copy = num.copy()
        for i in range(3):
            if guess[i] == num[i]:
                hit += 1
                num_copy.pop(i)
        for i in range(3):
            if num_copy[i] in guess:
                miss += 1
        print(f"{hit} hit {miss} miss.")


if __name__ == '__main__':
    main()
