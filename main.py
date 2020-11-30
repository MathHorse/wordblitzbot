from pynput.mouse import Button, Controller
import time
from pynput import keyboard
import os
mouse = Controller()

def on_press(key):
    if key == keyboard.Key.shift:
        os._exit(1)

listener = keyboard.Listener(
    on_press=on_press)
listener.start()

paths = [[y.split(',') for y in x.split(';')[:-1]] for x in open('paths.txt', 'r').readlines()[:-1]]
letters = [x.split(',') for x in open('letters.txt', 'r', encoding = 'utf-8').read().split(';')]
words = set([x.strip('\n') for x in open('magyar_szavak.txt', 'r').readlines()])
mouse_coords = [[int(y) for y in x.split(',')] for x in open('mousepos.txt', 'r').read().split(';')[:-1]]
print(mouse_coords)
print(letters)

voltmar = []
for path in paths:
    word = ''
    for tile in path:
        word += letters[int(tile[0])][int(tile[1])]
    if word in words and not word in voltmar:
        voltmar.append(word)
        time.sleep(0.05)
        mouse.position = mouse_coords[4 * int(path[0][0]) + int(path[0][1])]
        mouse.press(Button.left)
        for tile in path:
            time.sleep(0.05)
            mouse.position = mouse_coords[4 * int(tile[0]) + int(tile[1])]
        time.sleep(0.05)
        mouse.release(Button.left)
