import random
import time

import pyinputplus as pyip

while True:
    ####### UI
    base = [
        "-------------            -------------",
        "|   |   |   |            | 1 | 2 | 3 |",
        "|   |   |   |            | 4 | 5 | 6 |",
        "|   |   |   |            | 7 | 8 | 9 |",
        "-------------            -------------",
    ]
    example = """
        -------------
        | 1 | 2 | 3 |
        | 4 | 5 | 6 |
        | 7 | 8 | 9 |
        -------------
    """
    coords = ["", "1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3"]

    # FUNCTIONALITY
    main_list = [ba.split("|") for ba in base if ba.split("|")]


    def place_x_or_o(x: int, y: int, xoro: str):
        if main_list[x][y] == " x " or main_list[x][y] == " o ":
            for ba in base:
                print(ba)
            return print("position not available")
        else:
            main_list[x][y] = f" {xoro} "
            base[x] = "|".join(main_list[x])
            for ba in base:
                print(ba)
            return True


    # --------- THE COMMENTED AND THE ACTIVE "if_won()" FUNCTIONS WORK THE SAME ---------#

    # def if_won(x_or_o: str):
    #     if main_list[1][1] == x_or_o and main_list[1][2] == x_or_o and main_list[1][3] == x_or_o:
    #         return True
    #     elif main_list[2][1] == x_or_o and main_list[2][2] == x_or_o and main_list[2][3] == x_or_o:
    #         return True
    #     elif main_list[3][1] == x_or_o and main_list[3][2] == x_or_o and main_list[3][3] == x_or_o:
    #         return True
    #     elif main_list[1][1] == x_or_o and main_list[2][1] == x_or_o and main_list[3][1] == x_or_o:
    #         return True
    #     elif main_list[1][2] == x_or_o and main_list[2][2] == x_or_o and main_list[3][2] == x_or_o:
    #         return True
    #     elif main_list[1][3] == x_or_o and main_list[2][3] == x_or_o and main_list[3][3] == x_or_o:
    #         return True
    #     elif main_list[1][1] == x_or_o and main_list[2][2] == x_or_o and main_list[3][3] == x_or_o:
    #         return True
    #     elif main_list[1][3] == x_or_o and main_list[2][2] == x_or_o and main_list[3][1] == x_or_o:
    #         return True
    #     else:
    #         return False


    def if_won(x_or_o: str):
        for x in range(1, 4):
            if main_list[x][1] == x_or_o and main_list[x][2] == x_or_o and main_list[x][3] == x_or_o:
                return True
            elif main_list[1][x] == x_or_o and main_list[2][x] == x_or_o and main_list[3][x] == x_or_o:
                return True
        if main_list[1][1] == x_or_o and main_list[2][2] == x_or_o and main_list[3][3] == x_or_o:
            return True
        elif main_list[1][3] == x_or_o and main_list[2][2] == x_or_o and main_list[3][1] == x_or_o:
            return True
        else:
            return False


    def play_with_computer():
        play_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while True:
            val = "x"
            random_number = random.choice(play_list)
            print(f"computer ({val.upper()}) is playing...")
            time.sleep(1.5)
            if place_x_or_o(int(coords[random_number][0]), int(coords[random_number][2]), xoro=val):
                print("Computer just played!")
                play_list.remove(random_number)
                if if_won(f" {val} "):
                    print("Computer wins!")
                    time.sleep(2)
                    play = int(pyip.inputChoice(['0', '10'], prompt="Input '0' to restart, '10' to quit\n"))
                    return play
                if if_draw():
                    print("Draw!")
                    time.sleep(2)
                    play = int(pyip.inputChoice(['0', '10'], prompt="Input '0' to restart, '10' to quit\n"))
                    return play

            val = "o"
            print(f"Your turn ({val.upper()})")
            play = pyip.inputInt(
                "Input your position, e.g. '1' to play in the first box. Input '10' to quit, '0' to restart\n",
                min=0,
                max=10)
            if play == 10:
                return play
            elif play == 0:
                return play
            else:
                play_list.remove(play)
                if place_x_or_o(int(coords[play][0]), int(coords[play][2]), xoro=val):
                    if if_won(f" {val} "):
                        print("You win!")
                        time.sleep(2)
                        play = int(pyip.inputChoice(['0', '10'], prompt="Input '0' to restart, '10' to quit\n"))
                        return play
                    if if_draw():
                        print("Draw!")
                        time.sleep(2)
                        play = int(pyip.inputChoice(['0', '10'], prompt="Input '0' to restart, '10' to quit\n"))
                        return play
                else:
                    continue


    def if_draw():
        complete = 0
        for x in range(1, 4):
            try:
                if main_list[x][1].split()[0].isalpha() and main_list[x][2].split()[0].isalpha() and \
                        main_list[x][3].split()[0].isalpha():
                    complete += 1
                else:
                    return False
            except IndexError:
                continue
        if complete == 3:
            return True


    for ba in base:
        print(ba)
    val = "x"
    while True:
        print(f"{val.upper()}'s turn")
        play = pyip.inputInt(
            "Input your position, e.g. '1' to play in the first box. Input '10' to quit, '0' to restart and '11' to "
            "play with computer\n",
            min=0,
            max=11)
        if play == 10:
            break
        elif play == 0:
            break
        elif play == 11:
            play = play_with_computer()
            break
        else:
            if place_x_or_o(int(coords[play][0]), int(coords[play][2]), xoro=val):
                if if_won(f" {val} "):
                    print(f"{val.upper()} wins!")
                    time.sleep(2)
                    play = int(pyip.inputChoice(['0', '10'], prompt="Input '0' to restart, '10' to quit\n"))
                    break
                if if_draw():
                    print("Draw!")
                    time.sleep(2)
                    play = int(pyip.inputChoice(['0', '10'], prompt="Input '0' to restart, '10' to quit\n"))
                    break
                elif val == "o":
                    val = "x"
                elif val == "x":
                    val = "o"
            else:
                continue
    if play == 0:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nRESTARTING....\n\n\n\n\n")
        time.sleep(1)
        continue
    else:
        break
