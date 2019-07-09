import random
def hangman(word):

    wrong = 0
    stages = ["",
              "_________        ",
              "|                ",
              "|       |        ",
              "|       O        ",
              "|      /|\       ",
              "|      / \       ",
              "|                "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to the execution!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Enter the letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You won! The word was: {}.".format(word))
            print(" ".join(board))
            win = True
            break
    if not win:
        print("/n".join(stages[0: wrong]))
        print("You lost! The word was: {}.".format((word)))


dictionary = ["dog", "cat", "mouse", "door", "phone", "desk", "chair", "board", "book", "car", "ball", "bike", "house"]
hangman(dictionary[random.randint(0, 12)])
