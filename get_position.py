import pyautogui
import time

print("Move your mouse to the desired position and wait for 5 seconds...")
time.sleep(5)  # Gives you time to move the mouse to the desired position

current_position = pyautogui.position()
print(f"The current mouse position is: {current_position}")