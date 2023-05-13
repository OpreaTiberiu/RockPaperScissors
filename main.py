import random
import signs


rock = signs.rock
paper = signs.paper
scissors = signs.scissors
play = True
choice = int(input("What do you choose? \n 0 - Rock\n 1 - Paper\n 2 - Scissors\n 3 - Exit\n"))
if choice not in (0, 1, 2):
    play = False

while play:
    computer_choice = random.randint(0, 2)
    choice_array = [rock, paper, scissors]

    pick_one = choice_array[int(choice)].split('\n')
    pick_two = choice_array[int(computer_choice)].split('\n')

    output = ""
    # Revert the sign picked by the computer for better display
    for i in range(len(pick_one)):
        no_spaces = 40 - len(pick_one[i]) - len(pick_two[i])
        spaces = " "
        for j in range(no_spaces):
            spaces += " "
        output += pick_one[i] + spaces + pick_two[i][::-1].replace(')', '^').replace('(', ')').replace('^', '(') + "\n"

    print(output)

    win_pairs = [(0, 2), (1, 0), (2, 1)]
    lose_pairs = [(0, 1), (1, 2), (2, 0)]
    current_pair = (choice, computer_choice)

    if current_pair in win_pairs:
        print("You win!")
    elif current_pair in lose_pairs:
        print("You lose!")
    else:
        print("It's a draw!")

    choice = int(input("What do you choose? \n 0 - Rock\n 1 - Paper\n 2 - Scissors\n 3 - Exit\n"))
    if choice not in (0, 1, 2):
        play = False

