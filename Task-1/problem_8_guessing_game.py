import random


def main():
    # Generate a random number between 1 and 10.
    n = random.randint(1, 10)
    tries = 0
    while True:
        tries += 1
        if int(input()) == n:
            print(f"That's right! You got it in {tries}.")
            break
        else:
            print("Wrong guess.")


if __name__ == '__main__':
    main()
