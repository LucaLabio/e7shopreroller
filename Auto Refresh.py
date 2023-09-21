# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:19:03 2020

@author: Ema
"""


from pyautogui import *
import pyautogui
import time
import keyboard
###might use it later so that it clicks slightly off everytime
#import random 



#pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
#Scroll at semi random place
#Aprox place X: 1263 Y:  590
########

pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True
pantalla=pyautogui.size()
pyautogui.moveTo(pantalla[0]/2, pantalla[1]/2, duration=0)
contador=0
cont_coven=0
cont_mystic=0
cont_refresh=0

def locate():
    return pyautogui.locateOnScreen('refresh_button.PNG',confidence=0.90),\
            pyautogui.locateOnScreen('covenant.PNG',confidence=0.8899), \
            pyautogui.locateOnScreen('mystic.PNG', confidence=0.888)

def get_screen(png, confidance):
    return pyautogui.locateOnScreen(png, confidence=confidance)

def buy(pos,ypos,buybutton):
    time.sleep(0.3)
    point = pyautogui.center(pos)
    pyautogui.click(x=point[0] + 800, y=point[1] + ypos, clicks=2, interval=0.05, button='left')
    time.sleep(0.4)
    Buy_button_Covenant_pos = get_screen(buybutton, 0.95)
    Buy_button_Covenant_point = pyautogui.center(Buy_button_Covenant_pos)
    pyautogui.click(x=Buy_button_Covenant_point[0], y=Buy_button_Covenant_point[1], clicks=2, interval=0.05,
                    button='left')


def everything(Coven_pos, Mystic_pos, cont_coven, cont_mystic):
    # Checks for covenant
    if (Coven_pos) != None:
        print("Buy Covenant Summons.")
        buy(Coven_pos, 40, 'Buy_button_Covenant.PNG')
        cont_coven += 1

    time.sleep(0.05)

    # checks for mystic
    if (Mystic_pos) != None:
        print("Buy Mystic Summons.")
        buy(Mystic_pos, 50, 'Buy_button_Mystic.PNG')
        cont_mystic += 1

    return cont_coven, cont_mystic

def move_screen(cont_coven, cont_mystic):
    for i in range(2):
        pyautogui.moveTo(pantalla[0] / 2, pantalla[1] / 2, duration=0)
        # Drag upward 300 pixels in 0.2 seconds
        pyautogui.dragTo(pantalla[0] / 2, pantalla[1] / 2 - 300, duration=0.2)
        time.sleep(0.1)

        RB_pos, Coven_pos, Mystic_pos = locate()
        cont_coven, cont_mystic = everything(Coven_pos, Mystic_pos, cont_coven, cont_mystic)
    return cont_coven, cont_mystic

def refresh(RB_pos):
    RB_point = pyautogui.center(RB_pos)
    pyautogui.click(x=RB_point[0], y=RB_point[1], clicks=3, interval=0.05, button='left')
    time.sleep(0.5)  # wait for confirm to appear
    Confirm_pos = pyautogui.locateOnScreen('confirm button.PNG', confidence=0.90)
    Confirm_point = pyautogui.center(Confirm_pos)
    time.sleep(0.2)
    pyautogui.click(x=Confirm_point[0], y=Confirm_point[1], clicks=2, interval=0.05, button='left')

while keyboard.is_pressed('q') == False:
    RB_pos, Coven_pos, Mystic_pos = locate()

    refresh(RB_pos)

    cont_refresh += 1

    print("Covenant Summons bought=", cont_coven)
    print("Mystic Summons bought=", cont_mystic)
    print("Refresh Done=", cont_refresh)
    print("Spent Skystones=", cont_refresh*3)

    time.sleep(0.3)

    RB_pos, Coven_pos, Mystic_pos = locate()

    cont_coven,cont_mystic = everything(Coven_pos, Mystic_pos, cont_coven, cont_mystic)

    time.sleep(0.3)

    cont_coven, cont_mystic = move_screen(cont_coven, cont_mystic)

    time.sleep(0.3)




#%%Outside of the while loop
print("You exited successfuly")