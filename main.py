import random as r
import os


def game():
    gamers = eval(input("How many gamers? :"))
    ans = define_answer()
    round_count = 1
    gamer_count = 1
    history = []
    results = []
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # clear
        print(f"\nNow is gamer {gamer_count}'s turn")
        if round_count > 1:  # no data no output
            player_history = []
            player_results = []
            for i in range(gamer_count - 1, (round_count - 1) * gamers, gamers):
                player_history.append(history[i])
                player_results.append(results[i])
            screen(gamer_count, round_count, player_history, player_results)
        while True:
            guess = input("\nGuess: ")
            if not input_check(guess):  # invalid then guess again
                continue
            if not check_answer(ans=ans, guess=guess):  # guess not correct
                history.append(guess)
                result = check_AB(ans=ans, guess=guess)
                results.append(result)
                print(f"result: {result}")
                input("\nPress enter to continue...")
                break
            else:  # win
                print(f"<< Gamer {gamer_count} win >>")
                input("\nPress enter to continue...")
                return
        gamer_count += 1  # next gamer
        if gamer_count > gamers:  # cycle then next round
            gamer_count -= gamers
            round_count += 1


def screen(gamer, round_count, history, results):
    w = [7, 3, 3, 3, 3, 1, 6]
    print(f"gamer {gamer}: ")
    print()
    for i in range(0, round_count - 1):
        print(f"{f'round{i+1}':{w[0]}}|", end="")
        print(f"{f'{history[i][0]}':^{w[1]}}|", end="")
        print(f"{f'{history[i][1]}':^{w[2]}}|", end="")
        print(f"{f'{history[i][2]}':^{w[3]}}|", end="")
        print(f"{f'{history[i][3]}':^{w[4]}}|", end="")
        print(f"{f'':^{w[5]}}", end="")
        print(f"{f'{results[i]}':^{w[6]}}")


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

    B_count = B_count - A_count

    return f"{A_count}A{B_count}B"


def check_answer(ans, guess):
    if guess == ans:
        return True
    else:
        return False


def define_answer():
    while True:
        mode = input("[1]: Random\n[2]: Customize\n:")
        pool = [str(i) for i in range(10)]
        ans = ""
        if mode == "1":
            for _ in range(4):
                ans += r.choice(pool)
        elif mode == "2":
            try:
                temp = input("Customize: ")
                if input_check(temp):
                    ans = temp
            except Exception as e:
                print()
                continue
        else:
            print("Please try again.")
            continue
        return ans


def main():
    while True:
        new = input("[1]: New Game\n[2]: shutdown\n:")
        if new == "1":
            game()
        elif new == "2":
            print("Bye!")
            return
        else:
            print("Please try again.")


main()
