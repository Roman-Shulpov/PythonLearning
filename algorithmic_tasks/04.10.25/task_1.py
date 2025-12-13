import keyboard


def on_key(event):
    if event.name == 'down':
        print('Кажется ты нажал вниз.')
    elif event.name == 'right':
        print('Кажется ты нажал вправо.')
    elif event.name == 'up':
        print('Кажется ты нажал вверх.')
    elif event.name == 'left':
        print('Кажется ты нажал влево.')


keyboard.on_press(on_key)
print("Тыкай кнопки!")
keyboard.wait('esc')
