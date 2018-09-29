import pickle
from random import randint
import random
import time as t

score = [None] * 100
current_score = 0
time = 0
script = [None] * 100
character = [0,0] #[x,y]
board = [
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,3,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,2,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,4,0,0,0,0,2,0,1],
[1,0,2,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]
]

other_levels = [
[
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,1,2,1],
[1,0,0,0,0,0,0,3,0,1],
[1,0,0,0,0,0,0,1,0,1],
[1,0,0,0,0,0,0,1,0,1],
[1,0,0,0,0,0,0,1,0,1],
[1,0,0,0,0,0,0,1,2,1],
[1,1,1,1,1,1,1,1,0,1],
[1,4,0,0,0,0,2,0,0,1],
[1,1,1,1,1,1,1,1,1,1]
],
[
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,1,2,0,2,1,4,1],
[1,0,0,1,0,1,0,0,0,1],
[1,0,0,1,0,1,1,1,1,1],
[1,0,0,0,3,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]
],
[
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,1,1,1,0,1],
[1,0,0,0,0,0,4,0,2,1],
[1,0,0,0,0,1,1,1,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,3,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]
],
[
[1,1,1,1,1,1,1,1,1,1],
[1,4,0,1,0,0,2,0,0,1],
[1,1,0,1,0,1,1,1,0,1],
[1,0,2,1,2,1,0,1,0,1],
[1,0,1,1,0,1,0,1,2,1],
[1,0,1,0,0,1,0,1,0,1],
[1,0,1,3,1,1,0,1,0,1],
[1,2,1,1,1,1,1,1,0,1],
[1,0,0,0,2,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]
],
[
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,1,1,1,0,0,1],
[1,0,0,1,4,2,2,1,0,1],
[1,0,0,0,1,1,2,1,0,1],
[1,0,0,0,0,1,2,1,0,1],
[1,0,0,0,0,1,2,1,0,1],
[1,0,0,0,0,1,3,1,0,1],
[1,1,1,1,1,1,1,1,1,1]
],
[
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,1,0,0,0,1,1],
[1,0,0,0,1,0,1,4,0,1],
[1,3,0,0,1,0,1,1,0,1],
[1,0,1,1,1,0,0,0,0,1],
[1,2,0,1,1,1,2,1,0,1],
[1,1,0,1,0,0,0,1,0,1],
[1,1,2,1,1,1,1,1,2,1],
[1,0,0,0,2,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]
],
[
[1,1,1,1,1,1,1,1,1,1],
[1,1,0,0,0,1,0,0,4,1],
[1,0,0,1,0,0,2,1,0,1],
[1,1,2,0,0,1,0,0,0,1],
[1,0,0,1,0,0,0,1,0,1],
[1,1,0,0,0,1,0,0,0,1],
[1,0,0,1,2,0,0,1,0,1],
[1,1,0,0,0,1,0,2,0,1],
[1,3,0,1,2,0,0,1,0,1],
[1,1,1,1,1,1,1,1,1,1]
],
[
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,1,1,1,1],
[1,0,0,0,0,0,2,0,3,1],
[1,0,0,0,0,1,0,1,1,1],
[1,0,0,0,0,1,0,1,0,1],
[1,0,0,1,1,1,0,0,0,1],
[1,0,0,1,0,0,2,1,0,1],
[1,0,0,1,0,1,1,4,0,1],
[1,0,0,1,2,0,0,0,1,1],
[1,1,1,1,1,1,1,1,1,1]
],
[
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,1,0,2,0,1,0,1],
[1,0,0,1,0,1,0,4,1,1],
[1,0,0,1,2,0,1,1,0,1],
[1,0,0,0,1,0,1,0,0,1],
[1,0,0,0,1,0,1,0,0,1],
[1,0,0,0,1,0,1,0,0,1],
[1,0,0,0,1,0,1,0,0,1],
[1,0,0,3,0,2,1,0,0,1],
[1,1,1,1,1,1,1,1,1,1]
],
[
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,0,0,0,0,1],
[1,0,0,0,4,1,0,0,0,1],
[1,2,1,1,0,1,0,0,0,1],
[1,0,1,1,0,1,0,0,0,1],
[1,0,1,1,0,1,0,0,0,1],
[1,3,0,0,2,1,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]
]
]

def load_script(num):
    global script
    with open(str(num)+".script", 'rb') as f:
        script = pickle.load(f)

def write_script(num):
    global script
    with open(str(num)+".script", 'wb') as f:
        pickle.dump(script, f)

def load_board(num):
    global board
    with open(str(num)+".board", 'rb') as f:
        board = pickle.load(f)

def write_board(num):
    global board
    with open(str(num)+".board", 'wb') as f:
        pickle.dump(board, f)

def locate_char():
    global board
    for y, row in enumerate(board):
        for x, square in enumerate(row):
            if (square == 4):
                character[0] = x
                character[1] = y
                square = 0
                break

def up():
    global current_score
    global time
    if (board[character[1]-1][character[0]] == 0):
        board[character[1]][character[0]] = 0
        character[1] -= 1
        board[character[1]][character[0]] = 4
    elif (board[character[1]-1][character[0]] == 2):
        board[character[1]][character[0]] = 0
        current_score += 10
        character[1] -= 1
        board[character[1]][character[0]] = 4
    elif (board[character[1]-1][character[0]] == 3):
        current_score += 100
        time = 1

def down():
    global current_score
    global time
    if (board[character[1]+1][character[0]] == 0):
        board[character[1]][character[0]] = 0
        character[1] += 1
        board[character[1]][character[0]] = 4
    elif (board[character[1]+1][character[0]] == 2):
        board[character[1]][character[0]] = 0
        current_score += 10
        character[1] += 1
        board[character[1]][character[0]] = 4
    elif (board[character[1]+1][character[0]] == 3):
        current_score += 100
        time = 1

def left():
    global current_score
    global time
    if (board[character[1]][character[0]-1] == 0):
        board[character[1]][character[0]] = 0
        character[0] -= 1
        board[character[1]][character[0]] = 4
    elif (board[character[1]][character[0]-1] == 2):
        board[character[1]][character[0]] = 0
        current_score += 10
        character[0] -= 1
        board[character[1]][character[0]] = 4
    elif (board[character[1]][character[0]-1] == 3):
        current_score += 100
        time = 1

def right():
    global current_score
    global time
    if (board[character[1]][character[0]+1] == 0):
        board[character[1]][character[0]] = 0
        character[0] += 1
        board[character[1]][character[0]] = 4
    elif (board[character[1]][character[0]+1] == 2):
        board[character[1]][character[0]] = 0
        current_score += 10
        character[0] += 1
        board[character[1]][character[0]] = 4
    elif (board[character[1]][character[0]+1] == 3):
        current_score += 100
        time = 1

def jbu():
    if (board[character[1]-1] == 1):
        return True
    else:
        return False

def jcu():
    return not jbu()

def jbd():
    if (board[character[1]+1] == 1):
        return True
    else:
        return False

def jcd():
    return not jbd()

def jbl():
    if (board[character[0]-1] == 1):
        return True
    else:
        return False

def jcl():
    return not jbl()

def jbr():
    if (board[character[0]+1] == 1):
        return True
    else:
        return False

def jcr():
    return not jbr()

def run_script():
    global script
    global time
    i = 0
    time = 400
    locate_char()
    while (i < len(script)):
        if (time == 0):
            return
        line = script[i]
        t.sleep(.3)
        output = ""
        for row in board:
            output += "\n" + str(row)
        print(output)
        # print(line)
        # print(i)
        # print(time)
        if (line == "up"):
            up()
            i += 1
        elif (line == "down"):
            down()
            i += 1
        elif (line == "right"):
            right()
            i += 1
        elif (line == "left"):
            left()
            i += 1
        elif (line[:3] == "jbr"):
            if (jbr()):
                i = int(line[3:])
            else:
                i += 1
        elif (line[:3] == "jcr"):
            if (jcr()):
                i = int(line[3:])
            else:
                i += 1
        elif (line[:3] == "jbl"):
            if (jbl()):
                i = int(line[3:])
            else:
                i += 1
        elif (line[:3] == "jcl"):
            if (jcl()):
                i = int(line[3:])
            else:
                i += 1
        elif (line[:3] == "jbu"):
            if (jbu()):
                i = int(line[3:])
            else:
                i += 1
        elif (line[:3] == "jcu"):
            if (jcu()):
                i = int(line[3:])
            else:
                i += 1
        elif (line[:3] == "jbd"):
            if (jbd()):
                i = int(line[3:])
            else:
                i += 1
        elif (line[:3] == "jcd"):
            if (jcd()):
                i = int(line[3:])
            else:
                i += 1
        else:
            i += 1

        time -= 1

def test_generation():
    global current_score
    global score
    for genome in range(100):
        load_script(genome)
        current_score = 0
        for maze in range(10):
            load_board(maze)
            run_script()
        score[genome] = current_score
    print(score)

def random_line():
    command = random.choice(["up","down","right","left","jbr","jcr","jbl","jcl","jbu","jcu","jbd","jcd"])
    if (command[0] == 'j'):
        command += str(randint(0,100))
    return command

def breed(best, next_best, mutate_amount):
    global script
    load_script(best)
    slice = script[randint(0,100):randint(0,100)]
    load_script(next_best)
    start = randint(0,(100-len(slice)))
    script[start : start+len(slice)] = slice
    for i in range(mutate_amount):
        script[randint(0,99)] = random_line()

def evolve():
    global score
    best = score.index(max(score))
    score[best] = -1
    next_best = score.index(max(score))
    load_script(best)
    write_script(0)
    load_script(next_best)
    write_script(1)
    for child in range(2,100):
        breed(best, next_best, child)
        write_script(child)

def generate_script():
    for line in range(100):
        script[line] = random_line()

def initial_batch():
    global board
    global other_levels
    for genome in range(100):
        generate_script()
        write_script(genome)
    for num, level in enumerate(other_levels):
        board = level
        # print("")
        # for row in board:
        #     print(row)
        write_board(num)

def main():
    i = 0
    write_board(0)
    initial_batch()
    while (i<1000):
        test_generation()
        evolve()
        i += 1

def demo_run():
    load_script(0)
    for level in range(10):
        load_board(9)
        run_script()

# main()
demo_run()
