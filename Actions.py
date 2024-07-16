from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
import time
from Coordenates import *

#Links mouse to controller
pointer = Controller()
seeker = mouse.Controller()
teclado = keyboard.Controller()

#Callbacks
def first_click(var):
    global current
    current = seeker.position
    if ( var==left or var==rigth):
        pointer.position = (brackets)
        pointer.press(Button.left,)
        pointer.release(Button.left)
        time.sleep(brackets_delay)
        pointer.position = (var)
        pointer.press(Button.left,)
        pointer.release(Button.left)
    elif var:
        pointer.position = (var)
        pointer.press(Button.left,)
        pointer.release(Button.left)

def middle_click(var, num):
    time.sleep(num)
    pointer.position = (var)
    pointer.press(Button.left)
    pointer.release(Button.left)

def closing_click(var):
    pointer.position = var
    pointer.press(Button.left)
    pointer.release(Button.left)

def reposition():
    a = "a"

def final_click(num):
    pointer.position = (current)
    time.sleep(num)
    pointer.press(Button.left)
    pointer.release(Button.left)

def bug_spray(bug):
    teclado.release(bug)
    teclado.release(keyboard.Key.alt_l) 

def only_sizes(var, size, bug):
    first_click(var)
    middle_click(width, 0)
    middle_click(size, width_delay)
    closing_click(width)
    final_click(closind_delay)
    bug_spray(bug)

# One function to rule them all
def action(tool, new_width, new_color, bug, click):
    first_click(tool)
    #if width needs to be changed
    if new_width:
        pointer.position = width
        pointer.press(Button.left)
        pointer.release(Button.left)
        time.sleep(width_delay)
        pointer.position = new_width
        pointer.press(Button.left)
        pointer.release(Button.left)
        #if color also needs to be changed
        if new_color:
            pointer.position = color
            pointer.press(Button.left)
            pointer.release(Button.left)
            time.sleep(color_delay)
            pointer.position = new_color
            pointer.press(Button.left)
            pointer.release(Button.left)
            closing_click(color)
            if click:
                final_click(0.4)
                bug_spray(bug)
            else:
                pointer.position = (current)
                bug_spray(bug)
        #if only width was enough 
        else:
            closing_click(width)
            if click:
                final_click(0.2)
                bug_spray(bug)
            else:
                pointer.position = (current)
                bug_spray(bug)
    #if only color needs to be changed
    elif new_color:
        pointer.position = color
        pointer.press(Button.left)
        pointer.release(Button.left)
        time.sleep(color_delay)
        pointer.position = new_color
        pointer.press(Button.left)
        pointer.release(Button.left)
        closing_click(color)
        if click:
            final_click(0.2)
            bug_spray(bug)
        else:
            pointer.position = (current)
            bug_spray(bug)
    #if nothing needs to be further changed
    else:
        if click:
            final_click(0.2)
            bug_spray(bug)
        else:
            pointer.position = (current)
            bug_spray(bug)





