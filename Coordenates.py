from pynput import mouse
from pynput.mouse import Controller

#Positions
current = []
base_line = 190
second_line = 250
underline = [180, base_line]
marker = [275, base_line]
border = [225, base_line]
pen = [325, base_line]
rubber = [370, base_line]
x = [513, base_line]
check = [465, base_line]
brackets = [560 ,base_line]   
color = [754 , base_line]
width = [800 , base_line]
large = [738, second_line]
medium = [781, second_line]
small = [826, second_line]
tiny = [865, second_line]
left = [540, second_line]
rigth = [590, second_line]
red = [768, 516]
green = [741, 491]
purple = [688, 517]
orange = [662, 491]
yellow = [714, 492]
others = [610, base_line]
coma = [479, second_line]
dot = [434, second_line]
grave = [609, second_line]
agudo = [565, second_line]
circunflexo = [654, second_line]
til = [700, second_line]

#Delays
other_delay = 0.
brackets_delay = 0.1
color_delay = 0.3
width_delay = 0.3
closind_delay = 0.2

#Finder
pointer = Controller()
seeker = mouse.Controller()
print(seeker.position)
