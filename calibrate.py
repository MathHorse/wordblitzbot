from pynput.mouse import Button, Controller
from pynput import keyboard
mouse = Controller()

globals()['ms'] = []

def on_press(key):
    if key == keyboard.Key.esc:
        listener.stop()
    if key == keyboard.Key.shift:
        globals()['ms'].append(mouse.position)
        print(mouse.position)

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

with open('mousepos.txt', 'w') as f:
    for i in globals()['ms']:
        f.write(f'{i[0]},{i[1]};')
