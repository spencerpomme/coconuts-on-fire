# implementation of card game - Memory 2D

import simpleguitk as simplegui
import random

num = []

state = 0
pre_x_index, pre_y_index = 0, 0
after_x_index, after_y_index = 0, 0

turn = 0

# helper function to initialize globals
def new_game():
    global num, exposed, turn
    prenum = list(range(0, 8))
    prenum.extend(list(range(0, 8)))
    random.shuffle(prenum)
    for n in range(0, 4):
        num.append(prenum[0:4])
        for m in range(0, 4):
            prenum.pop(0)

    exposed = [[False, False, False, False], [False, False, False, False], [False, False, False, False],
               [False, False, False, False]]

    turn = 0
    print("num =", num)


# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, turn, pre_x_index, pre_y_index, after_x_index, after_y_index, state
    x_index, y_index = pos[1] // 100, pos[0] // 100

    if not exposed[x_index][y_index]:
        exposed[x_index][y_index] = True
        if state == 0:
            state = 1
            pre_x_index, pre_y_index = x_index, y_index
        elif state == 1:
            state = 2
            after_x_index, after_y_index = x_index, y_index
        elif state == 2:
            if num[pre_x_index][pre_y_index] != num[after_x_index][after_y_index]:
                exposed[pre_x_index][pre_y_index] = False
                exposed[after_x_index][after_y_index] = False
            pre_x_index, pre_y_index = x_index, y_index
            state = 1
        turn += 1

        print("state:", state)
        print("click pos:", pos)
        print("number:", num[x_index][y_index])


# cards are logically 100x100 pixels in size    

# draw method to test
def draw(canvas):
    global num
    label.set_text("Moves = " + str(turn))
    # The sequece of x_index and y_index can have slight difference when projecting numbers in the matrix
    yoffset = 0
    x_index = 0
    for col in range(0, 4):
        xoffset = 0
        y_index = 0
        for row in range(0, 4):
            if exposed[x_index][y_index]:
                canvas.draw_text(str(num[x_index][y_index]), (xoffset + 25, yoffset + 100), 80, "White")

            else:
                canvas.draw_polygon([(xoffset, yoffset), (xoffset, yoffset + 100), (xoffset + 100, yoffset + 100),
                                     (xoffset + 100, yoffset)], 1, "Black", "Green")
            xoffset += 100
            y_index += 1
        yoffset += 100
        x_index += 1
        # print("x_index is:", x_index, "y_index is:", y_index)


# create frame and add a button and labels
frame = simplegui.create_frame("Memory 2.0", 400, 400)
frame.add_button("Reset Game", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()

frame.start()
# Always remember to review the grading rubric
