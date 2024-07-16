from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
import time
from Coordenates import *
import Actions



def on_activate_x():
    Actions.first_click(x)
    Actions.middle_click(width, 0)
    Actions.middle_click(small, width_delay)
    Actions.closing_click(width)
    Actions.final_click(closind_delay)
    Actions.bug_spray('m')

def on_activate_check():
    Actions.first_click(check)
    Actions.middle_click(width, 0)
    Actions.middle_click(medium, width_delay)
    Actions.final_click(closind_delay)
    Actions.bug_spray('n')

def on_activate_rubber():
    Actions.first_click(rubber)
    Actions.final_click(0)
    Actions.bug_spray('b')

def on_activate_pen():
    Actions.first_click(pen)
    Actions.middle_click(width, 0)
    Actions.middle_click(tiny, width_delay)
    Actions.final_click(0)
    Actions.bug_spray("v")

def on_activate_marker():
    Actions.first_click(marker)
    Actions.final_click(0)
    Actions.bug_spray('c')

def on_activate_border():
    Actions.first_click(border)
    Actions.middle_click(width, 0)
    Actions.middle_click(tiny, width_delay)
    Actions.closing_click(width)
    Actions.final_click(0)
    Actions.bug_spray('x')

def on_activate_underline():
    Actions.first_click(underline)
    Actions.middle_click(width, 0)
    Actions.middle_click(tiny, width_delay)
    Actions.final_click(0)
    Actions.bug_spray('z')

def on_activate_dot():
    Actions.first_click(color)
    Actions.middle_click(red, color_delay)
    Actions.middle_click(width, width_delay)
    Actions.middle_click(medium, width_delay)
    Actions.final_click(0)
    Actions.bug_spray('1')

def on_activate_coma():
    Actions.first_click(color)
    Actions.middle_click(red, color_delay)
    Actions.middle_click(width, width_delay)
    Actions.middle_click(medium, width_delay)
    Actions.final_click(0)
    Actions.bug_spray('2')

def on_activate_agudo():
    Actions.first_click(color)
    Actions.middle_click(red, color_delay)
    Actions.middle_click(width, width_delay)
    Actions.middle_click(medium, width_delay)
    Actions.final_click(0)
    Actions.bug_spray('4')

def on_activate_grave():
    Actions.first_click(color)
    Actions.middle_click(red, color_delay)
    Actions.middle_click(width, width_delay)
    Actions.middle_click(medium, width_delay)
    Actions.final_click(0)
    Actions.bug_spray('5')

def on_activate_circunflexo():
    Actions.first_click(color)
    Actions.middle_click(red, color_delay)
    Actions.middle_click(width, width_delay)
    Actions.middle_click(medium, width_delay)
    Actions.final_click(0)
    Actions.bug_spray('6')

def on_activate_til():
    Actions.first_click(color)
    Actions.middle_click(red, color_delay)
    Actions.middle_click(width, width_delay)
    Actions.middle_click(medium, width_delay)
    Actions.final_click(0)
    Actions.bug_spray('7')

def on_activate_bracket_left():
    Actions.first_click(brackets)
    Actions.middle_click(left, 0.05)
    Actions.middle_click(width, 0)
    Actions.middle_click(small, width_delay)
    Actions.middle_click(color, 0)
    Actions.middle_click(purple, color_delay)
    Actions.closing_click(color)
    Actions.final_click(0)

def on_activate_bracket_rigth():
    Actions.first_click(brackets)
    Actions.middle_click(rigth, brackets_delay)
    Actions.middle_click(color, 0)
    Actions.middle_click(purple, color_delay)
    Actions.middle_click(width, 0)
    Actions.middle_click(small, width_delay)
    Actions.closing_click(width)
    Actions.final_click(0)

def on_activate_yellow():
    Actions.first_click(color)
    Actions.middle_click(yellow, color_delay)
    Actions.closing_click(color)
    Actions.final_click(0)
    Actions.bug_spray('g')

def on_activate_orange():
    Actions.first_click(color)
    Actions.middle_click(orange, color_delay)
    Actions.closing_click(color)
    Actions.final_click(0)
    Actions.bug_spray('h')

def on_activate_purple():
    Actions.first_click(color)
    Actions.middle_click(purple, color_delay)
    Actions.closing_click(color)
    Actions.final_click(0)
    Actions.bug_spray('j')

def on_activate_green():
    Actions.first_click(color)
    Actions.middle_click(green, color_delay)
    Actions.closing_click(color)
    Actions.final_click(0)
    Actions.bug_spray('k')

def on_activate_red():
    Actions.first_click(color)
    Actions.middle_click(red, color_delay)
    Actions.closing_click(color)
    Actions.final_click(0)
    Actions.bug_spray('l')

def on_activate_small():
    Actions.first_click(width)
    Actions.middle_click(small, width_delay)
    Actions.closing_click(width)
    Actions.final_click(0)
    Actions.bug_spray('s')

def on_activate_medium():
    Actions.first_click(width)
    Actions.middle_click(medium, width_delay)
    Actions.closing_click(width)
    Actions.final_click(0)
    Actions.bug_spray('a')




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