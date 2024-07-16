from pynput import keyboard
from Coordenates import *
import Actions


# Functions

def on_activate_x():
    Actions.action(x, small, 0, "m", 1)
def on_activate_check():
    Actions.action(check, medium, 0, 'n', 1)
def on_activate_rubber():
    Actions.action(rubber, 0, 0, "b", 0)
def on_activate_pen():
    Actions.action(pen, tiny, red, 'v', 0)
def on_activate_marker():
    Actions.action(marker, 0, yellow, 'c', 0)
def on_activate_border():
    Actions.action(border, tiny, 0, 'x', 0)
def on_activate_underline():
    Actions.action(underline, tiny, 0, 'z', 0)
def on_activate_dot():
    Actions.action(0, medium, red, '1', 1)
def on_activate_coma():
    Actions.action(0, medium, red, '2', 1)
def on_activate_agudo():
    Actions.action(0, medium, red, '4', 1)
def on_activate_grave():
    Actions.action(0, medium, red, '5', 1)
def on_activate_circunflexo():
    Actions.action(0, medium, red, '6', 1)
def on_activate_til():
    Actions.action(0, small, red, '7', 1)
def on_activate_bracket_left():
    Actions.action(left, small, purple, '[', 0)
def on_activate_bracket_rigth():
    Actions.action(rigth, small, purple, ']', 0)
def on_activate_yellow():
    Actions.action(0, 0, yellow, 'g', 0)
def on_activate_orange():
    Actions.action(0, 0, orange, 'h', 0)
def on_activate_purple():
    Actions.action(0, 0, purple, 'j', 0)
def on_activate_green():
    Actions.action(0, 0, green, 'k', 0)
def on_activate_red():
    Actions.action(0, 0, red, 'l', 0)
def on_activate_small():
    Actions.action(0, small, 0, 's', 0)
def on_activate_medium():
    Actions.action(0, medium, 0, 'a', 0)



with keyboard.GlobalHotKeys({
        '<alt>+z': on_activate_underline,
        '<alt>+x': on_activate_border,
        '<alt>+c': on_activate_marker, 
        '<alt>+v': on_activate_pen,
        '<alt>+b': on_activate_rubber,
        '<alt>+n': on_activate_check,
        '<alt>+m': on_activate_x,
        '<alt>+1': on_activate_dot,
        '<alt>+2': on_activate_coma,
        '<alt>+4': on_activate_agudo,
        '<alt>+5': on_activate_grave,
        '<alt>+6': on_activate_circunflexo,
        '<alt>+7': on_activate_til,
        '<alt>+g': on_activate_yellow,
        '<alt>+h': on_activate_orange,
        '<alt>+j': on_activate_purple,
        '<alt>+k': on_activate_green,
        '<alt>+l': on_activate_red,
        '<alt>+a': on_activate_medium,
        '<alt>+s': on_activate_small,
        '[': on_activate_bracket_left,
        ']': on_activate_bracket_rigth}) as h:
    h.join()