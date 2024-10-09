import random


def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:4]


def check_guess(guess, answer):
    A = 0
    B = 0
    for i in range(4):
        if guess[i] == answer[i]:
            A += 1
        elif guess[i] in answer:
            B += 1
    return A, B


def main():
    answer = generate_number()
    print("Welcome to the 1A2B guessing game!")
    while True:
        guess = input("Enter your guess (four digits): ")
        guess = [int(digit) for digit in guess]
        A, B = check_guess(guess, answer)
        print(f"{A}A{B}B")
        if A == 4:
            print("Congratulations! You've guessed the right number!")
            break


if __name__ == "__main__":
    main()
