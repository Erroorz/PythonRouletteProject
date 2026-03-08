#my silly lil program :3
#simple and easy to understand so small brain doesn't get overwhelmed (myself)

import random
colors = ["BLACK"] * 18 + ["RED"] * 18 + ["Green"]
is_active = True
has_lost = False
last_bet = False
balance = 0


def get_balance(squares, bet, deposit):
    money = (36 / squares) - 1
    payout = bet * money
    balance = payout + deposit
    print("Congratulations!!!")
    print(f"You have won: {payout}€")
    print(f"Your balance: {balance}€")
    return balance

def get_payout(squares, bet):
    money = (36 / squares) - 1
    payout = bet * money
    return payout


print("*****************************")
print("Welcome to SimplerRoulette!  ")
print("    (European version)       ")
print("*****************************")
print("How much money you want to deposit? ")
deposit = (input("enter amount here:"))
deposit = int(deposit)
if deposit <= 0:
    print("Enter a positive number and try again please")
    is_active = False

balance += deposit
print(f"Your balance is now worth: {balance}€")
bet = (input("enter a bet amount here:"))
bet = int(bet)
while is_active:
    new_balance = 0

    if balance <= 0:
        print("Sorry, you don't have any money left in your balance")
        is_active = False
    else:
        if balance == bet:
            last_bet = True
        balance -= bet
        print(f"The rest of your balance is now worth: {balance}€ and your bet is set at: {bet}€.")

    rannum = random.randint(0, 36)
    rancol = random.choice(colors)
    # I know that certain number are certain colors but the player is never going to see both variables at the same time so no need to implement that I think
    print("*****************************")
    print("Here is a list of bet choices")
    print("*****************************")
    print("1.  * Color (RED or BLACK) *")
    print("2.  * Even number * ")
    print("3.  * Odd number *")
    print("4.  * High number (19-36) * ")
    print("5.  * First 1-12 (1-12) * ")
    print("6.  * Second 12 (13-24) * ")
    print("7.  * Third 12 (25-36) * ")
    print("8.  * First column * ")
    print("9.  * Second column * ")
    print("10. * Third column * ")
    print("11. * Straight (single number) * ")
    print("12. * Split (two numbers) * ")
    print("13. * Street (three numbers) * ")
    print("14. * Corner (four numbers) * ")
    print("15. * Straight double (six numbers) * ")
    print("*********************************")
    print()
    print("Which option would you like to bet on?")
    bet_choice = (input("Enter the number of a bet option shown in the chart: "))
    bet_choice = int(bet_choice)

    if bet_choice < 0 or bet_choice > 16:
        print("Your bet choice is invalid")
        is_active = False

    print(f"Your bet choice was: {bet_choice}")
    print("Good luck!")

    if bet_choice == 1:
        col_choice = input("Choose either RED or BLACK:").upper()
        if col_choice == rancol:
            get_payout(18, bet)
            get_balance(18, bet, deposit)
        else:
            print("The color was", rancol)
            print(f"Sorry u lost {bet}€, better luck next time! :)")


    elif bet_choice == 2:
        if rannum % 2 == 0:
            print("The number is even")
            get_payout(18, bet)
            get_balance(18, bet, deposit)
        else:
            print("The number was", rannum)
            print(f"Sorry u lost {bet}€, better luck next time! :)")
            has_lost = True

    elif bet_choice == 3:
        if rannum % 1 == 0:
            print("The number is odd")
            get_payout(18, bet)
            get_balance(18, bet, deposit)
        else:
            print("The number was", rannum)
            print(f"Sorry u lost {bet}€, better luck next time! :)")
            has_lost = True

    elif bet_choice == 4:
        if rannum <= 36 and rannum > 19:
            print("The number is between 19 and 36")
            get_payout(17, bet)
            get_balance(17, bet, deposit)
        else:
            print("The number was", rannum)
            print(f"Sorry u lost {bet}€, better luck next time! :)")
            has_lost = True

    elif bet_choice == 5:
        if rannum >= 1 and rannum <= 12:
            print("The number is between 1 and 12")
            get_payout(12, bet)
            get_balance(12, bet, deposit)
        else:
            print("The number was", rannum)
            print(f"Sorry u lost {bet}€, better luck next time! :)")
            has_lost = True

    elif bet_choice == 5:
        if rannum >= 13 and rannum <= 24:
            print("The number is between 13 and 24")
            get_payout(12, bet)
            get_balance(12, bet, deposit)
        else:
            print("The number was", rannum)
            print("Sorry u lost, better luck next time! :)")
            has_lost = True
    elif bet_choice == 6:
        if rannum >= 13 and rannum <= 24:
            print("The number is between 13 and 24")
            get_payout(12, bet)
            get_balance(12, bet, deposit)
        else:
            print("The number was", rannum)
            print("Sorry u lost, better luck next time! :)")
            has_lost = True

    elif bet_choice == 7:
        if 25 <= rannum <= 36:
            print("The number is between 25 and 36")
            get_payout(12, bet)
            get_balance(12, bet, deposit)
        else:
            print("The number was", rannum)
            print(f"Sorry u lost {bet}€, better luck next time! :)")
            has_lost = True

    if bet_choice == 8:
        fir_col = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
        if rannum in fir_col:
            print(fir_col)
            print("The number was in the first column")
            get_payout(12, bet)
            get_balance(12, bet, deposit)
        else:
            print("The number was", rannum)
            print(fir_col)
            print(f"Sorry u lost {bet}€, better luck next time! :)")
            has_lost = True

    if bet_choice == 9:
        sec_col = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
        if rannum in sec_col:
            print(sec_col)
            print("The number was in the second column")
            get_payout(12, bet)
            get_balance(12, bet, deposit)
        else:
            print("The number was", rannum)
            print(sec_col)
            print(f"Sorry u lost {bet}€, better luck next time! :)")
            has_lost = True

    if bet_choice == 10:
        thi_col = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
        if rannum in thi_col:
            print(thi_col)
            print("The number was in the third column")
            get_payout(12, bet)
            get_balance(12, bet, deposit)
        else:
            print("The number was", rannum)
            print(thi_col)
            print(f"Sorry u lost {bet}€, better luck next time! :)")
            has_lost = True

    elif bet_choice == 11:
        num_choice = int(input("Choose a single number to bet on:"))
        if num_choice == rannum:
            get_payout(1, bet)
            get_balance(1, bet, deposit)
        else:
            print("The number was", rannum)
            print(f"Sorry u lost {bet}€, better luck next time! :)")
            has_lost = True

    elif bet_choice == 12:
        choices = []
        num_choice1 = int(input("Choose first numbers to bet on:"))
        if num_choice1 > 36 or num_choice1 < 0:
            print("invalid number")
        else: choices.append(num_choice1)
        num_choice2 = int(input("Choose second numbers to bet on:"))
        if num_choice2 > 36 or num_choice2 < 0:
            print("invalid number")
        else:
            choices.append(num_choice2)
        if rannum in choices:
            get_payout(2, bet)
            get_balance(2, bet, deposit)
        else:
            print("The number was", rannum)
            print(f"Sorry u lost {bet}€, better luck next time! :)")
            has_lost = True

    elif bet_choice == 13:
        choices = []
        num_choice1 = int(input("Choose first numbers to bet on:"))
        if num_choice1 > 36 or num_choice1 < 0:
            print("invalid number")
        else:
            choices.append(num_choice1)
        num_choice2 = int(input("Choose second numbers to bet on:"))
        if num_choice2 > 36 or num_choice2 < 0:
            print("invalid number")
        else:
            choices.append(num_choice2)
        num_choice3 = int(input("Choose third numbers to bet on:"))
        if num_choice3 > 36 or num_choice3 < 0:
            print("invalid number")
        else:
            choices.append(num_choice3)

        if rannum in choices:
            get_payout(3, bet)
            get_balance(3, bet, deposit)
        else:
            print("The number was", rannum)
            print(f"Sorry u lost {bet}€, better luck next time! :)")
            has_lost = True

    elif bet_choice == 14:
        choices = []
        num_choice1 = int(input("Choose first numbers to bet on:"))
        if num_choice1 > 36 or num_choice1 < 0:
            print("invalid number")
        else:
            choices.append(num_choice1)
        num_choice2 = int(input("Choose second numbers to bet on:"))
        if num_choice2 > 36 or num_choice2 < 0:
            print("invalid number")
        else:
            choices.append(num_choice2)
        num_choice3 = int(input("Choose third numbers to bet on:"))
        if num_choice3 > 36 or num_choice3 < 0:
                print("invalid number")
        else:
            choices.append(num_choice3)
        num_choice4 = int(input("Choose fourth numbers to bet on:"))
        if num_choice4 > 36 or num_choice4 < 0:
                print("invalid number")
        else:
            choices.append(num_choice4)
        if rannum in choices:
            get_payout(4, bet)
            get_balance(4, bet, deposit)
        else:
            print("The number was", rannum)
            print(f"Sorry u lost {bet}€, better luck next time! :)")
            has_lost = True

    elif bet_choice == 15:
        choices = []
        num_choice1 = int(input("Choose first numbers to bet on:"))
        if num_choice1 > 36 or num_choice1 < 0:
            print("invalid number")
        else:
            choices.append(num_choice1)
        num_choice2 = int(input("Choose second numbers to bet on:"))
        if num_choice2 > 36 or num_choice2 < 0:
            print("invalid number")
        else: choices.append(num_choice2)
        num_choice3 = int(input("Choose third numbers to bet on:"))
        if num_choice3 > 36 or num_choice3 < 0:
                print("invalid number")
        else:
            choices.append(num_choice3)
        num_choice4 = int(input("Choose fourth numbers to bet on:"))
        if num_choice4 > 36 or num_choice4 < 0:
                print("invalid number")
        else:
            choices.append(num_choice4)
        num_choice5 = int(input("Choose fifth numbers to bet on:"))
        if num_choice5 > 36 or num_choice5 < 0:
                print("invalid number")
        else:
            choices.append(num_choice5)
        num_choice6 = int(input("Choose sixth numbers to bet on:"))
        if num_choice6 > 36 or num_choice6 < 0:
                print("invalid number")
        else:
            choices.append(num_choice6)
        if rannum in choices:
            get_payout(6, bet)
            get_balance(6, bet, deposit)
        else:
            print("The number was", rannum)
            print(f"Sorry u lost {bet}€, better luck next time! :)")
            has_lost = True

    if balance <= 0:
        print("Sorry, you don't have any money left in your balance")
        is_active = False

    if has_lost and last_bet:
        print("Sorry, you don't have any money left in your balance")
        is_active = False
    else:
        print("keep playing? y/n")
        play_choice = input().lower()
        if play_choice == "n":
            print("Thank you for playing!")
            is_active = False
        else:
            if has_lost:
               print(f"Your balance is {balance}€")
               bet = int(input("Set a new bet to:"))
               if bet <= 0:
                   print("Enter a positive number and try again please")
                   is_active = False
            else:
                print(f"Your balance is {balance}€")
                bet = int(input("Set a new bet to:"))
                if bet <= 0:
                    print("Enter a positive number and try again please")
                    is_active = False
