import keyboard
import os

rows, cols = 10, 10
x, y = 0, 0

def clear_screen():
    os.system('cls')

def print_field():
    clear_screen()
    for i in range(rows):
        for j in range(cols):
            if i == y and j == x:
                print('⬛', end='')
            else:
                print('⬜', end='')
        print()

def on_key(event):
    global x, y

    if event.name == 'up' and y > 0:
        y -= 1
    elif event.name == 'down' and y < rows - 1:
        y += 1
    elif event.name == 'left' and x > 0:
        x -= 1
    elif event.name == 'right' and x < cols - 1:
        x += 1
    else:
        return

    print_field()


print_field()
print("Управляй стрелками. Выход — Esc")

keyboard.on_press(on_key)
keyboard.wait('esc')
