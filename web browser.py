import serial
import time
import pyautogui

ser= serial.Serial('COM3',9600)
time.sleep(3)
while 1:

    val =str( ser.readline() )


    if 'Scroll_Up' in val :
        pyautogui.typewrite(['up'])
        print(val)

    if 'Scroll_Down' in val :
        pyautogui.typewrite(['down'])
        print(val)

    if 'Forward' in val :
        pyautogui.typewrite(['alt','right'])
        print(val)

    if 'Rewind' in val :
        pyautogui.typewrite(['alt','left'])
        print(val)

    if 'Change_Tab' in val:
        pyautogui.hotkey('ctrl','tab')
        print(val)

    if 'Enter' in val:
        pyautogui.typewrite(['enter'])
        print(val)

   
