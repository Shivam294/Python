import pyautogui as gui
import time

time.sleep(5)

current_position = gui.position()
print(f"Current mouse position: {current_position}")
x,y = 100, 200

for i in range (0,100):
    gui.moveTo(x+i,y+i,duration=10000)
gui.click()