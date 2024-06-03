import random as r


def game():
    gamers = eval(input("How many gamers? :"))
    ans = define_answer()
    round_count = 1
    gamer_count = 1
    history = []
    results = []
    while True:
        print(f"Now is gamer {gamer_count}'s turn")
        while True:
            guess = input("Guess: ")
            if not input_check(guess):
                print("Invalid")
                continue
            if not check_answer(ans=ans, guess=guess):
                history.append(guess)
                result = check_AB(ans=ans, guess=guess)
                results.append(result)
                screen(gamer_count, round_count, history, results)


def screen(gamer, round_count, history, result):
    w = [7, 3, 3, 3, 3, 1, 6]
    print(f"gamer {gamer}:")
    print()
    for i in range(0, round_count):
        print(f"{f'round{i+1}':{w[0]}}|", end="")
        print(f"{f'{history[i][0]}':^{w[1]}}|", end="")
        print(f"{f'{history[i][1]}':^{w[2]}}|", end="")
        print(f"{f'{history[i][2]}':^{w[3]}}|", end="")
        print(f"{f'{history[i][3]}':^{w[4]}}|", end="")
        print(f"{f'':^{w[5]}}", end="")
        print(f"{f'{result[i]}':^{w[6]}}")


def input_check(ans):
    if len(ans) != 4:
        print("We need four digits")
        return False
    if not ans.isdigit():
        print("Please enter digits.")
        return False
    return True


def check_AB(ans, guess):
    A_count = 0
    B_count = 0
    for i in range(4):
        if guess[i] == ans[i]:
            A_count += 1

    for i in ans:
        for j in guess:
            if i == j:
                B_count += 1
                ans = ans.replace(i, "_", 1)
                guess = guess.replace(j, "_", 1)
                break

    return f"{A_count}A{B_count}B"


def check_answer(ans, guess):
    if guess == ans:
        return True
    else:
        return False


def define_answer():
    while True:
        mode = input("[1]: Random\n[2]: Customize\n:")
        pool = [str(i) for i in range(11)]
        ans = ""
        if mode == "1":
            for _ in range(4):
                ans += r.choice(pool)
        if mode == "2":
            try:
                temp = input(":")
                if input_check(temp):
                    ans = temp
            except Exception as e:
                print()
        else:
            print("Please try again.")
        return ans


def main():
    while True:
        new = input("[1]: New Game\n[2]: shutdown\n:")
        if new == "1":
            pass
        elif new == "2":
            print("Bye!")
            return
        else:
            print("Please try again.")


main()
