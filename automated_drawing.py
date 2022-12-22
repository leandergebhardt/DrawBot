import pyautogui
# X & Y axis
print(pyautogui.size())
# Do some stuff
# print(pyautogui.position())


distance = 400 # distance per line
while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5, button='left')   # move right
        distance -= 25
        pyautogui.drag(0, distance, duration=0.5,button='left')   # move down
        pyautogui.drag(-distance, 0, duration=0.5,button='left')  # move left
        distance -= 25
        pyautogui.drag(0, -distance, duration=0.5,button='left')  # move up