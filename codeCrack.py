import pyautogui as p
import time as t

delay = 0
pos1 = (924, 400)
pos2 = (1081, 623)

with open("four-digit-pin-codes-sorted-by-frequency-withcount copy.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    t.sleep(delay / 1000)
    p.moveTo(*pos1, duration=0.0)
    print(line)
    p.click(duration=0.0)
        
    p.typewrite(line, interval=0.0)
    p.moveTo(*pos2, duration=0.0)
    p.click(clicks=4, interval=0.0)