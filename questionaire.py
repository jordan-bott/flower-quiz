from flowers import flowers

print("\nWelcome to the flower quiz! Type in the number that best matches your answer for each question.")
choice_1 = None
while choice_1 not in ('1', '2', '3', '4', '5', '6'):
    choice_1 = input("\nWhat is your favorite color?\n (1)Red (2)Orange (3)Yellow (4)Green (5)Blue (6)Purple\t")
    # red, orange, yellow, green, blue, purple
choice_2 = None
while choice_2 not in ('1', '2', '3', '4', '5', '6'):
    choice_2 = input("\nHow are you feeling today?\n (1)Happy (2)Sad (3)Silly (4)Mad (5)Crazy (6)Fine\t")
    # happy, sad, silly, mad, crazy, fine
choice_3 = None
while choice_3 not in ('1', '2', '3', '4'):
    choice_3 = input("\nChoose a food from the list below\n (1)Pizza (2)Sushi (3)Spaghetti (4)Cheeseburger\t")
    # pizza, sushi, spaghetti, cheeseburger
choice_4 = None
while choice_4 not in ('1', '2', '3', '4'):
    choice_4 = input("\nHow many siblings do you have?\n (1)1 (2)2 (3)3+ (4)0\t")
    # 0, 1, 2, 3+
choice_5 = None
while choice_5 not in ('1', '2', '3', '4'):
    choice_5 = input("\nWhat's your favorite season?\n (1)Spring (2)Summer (3)Autumn (4)Winter\t")
    # spring, summer, autumn, winter

i1 = int(choice_1) - 1
i2 = int(choice_2) - 1
i3 = int(choice_3) - 1
i4 = int(choice_4) - 1
i5 = int(choice_5) - 1

print(f"\n\nYour flower is \033[1m{flowers[i1][i2][i3][i4][i5]}\033[0m! Thanks for playing!\n\n")
