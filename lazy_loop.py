import pyautogui
import time
from datetime import datetime

def open_browser_and_navigate():
    pyautogui.click(x=-1528, y=-70)
    time.sleep(1)

def copy_table_template():
    pyautogui.click(x=-1634, y=687)
    time.sleep(1)
    pyautogui.click(x=-1258, y=442) 
    time.sleep(0.5)
    pyautogui.hotkey('command', 'c') 

def paste_table_and_update_date():
    pyautogui.click(x=-1609, y=475)
    time.sleep(1)
    pyautogui.click(x=-1235, y=400)
    time.sleep(0.5)
    pyautogui.hotkey('command', 'v')

    # Update the date
    pyautogui.click(x=-1237, y=348)
    today_date = datetime.now()
    formatted_date = today_date.strftime('%Y.%m.%d')
    pyautogui.write(formatted_date)

def main():
    open_browser_and_navigate()
    copy_table_template()
    paste_table_and_update_date()

if __name__ == "__main__":
    main()