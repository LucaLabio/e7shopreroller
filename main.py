import sys
import time

import keyboard
import pyautogui

from helpers import helper

REFRESH_BUTTON_PATH = "images/ui/refresh_button.PNG"
REFRESH_CONFIDENCE = 0.90
SUMMON_CONFIDENCE = 0.97


def get_data():
    coven_pos = helper.locate("images/covenant/covenant.PNG", SUMMON_CONFIDENCE)
    mystic_pos = helper.locate("images/mystic/mystic.PNG", SUMMON_CONFIDENCE)
    screen_reader = helper.read_text()

    return coven_pos, mystic_pos, screen_reader


def main():
    refresh_button_pos = pyautogui.locateOnScreen(
        REFRESH_BUTTON_PATH, confidence=REFRESH_CONFIDENCE
    )
    if refresh_button_pos is None:
        print("Error: Unable to find reroll button")
        sys.exit(1)

    refresh_count = 0

    while not keyboard.is_pressed("q"):
        coven_pos, mystic_pos, screen_reader = get_data()
        coven_bought, mystic_bought = helper.check(
            coven_pos, mystic_pos, screen_reader
        )

        helper.move_screen()
        time.sleep(0.4)

        if not (coven_bought and mystic_bought):
            coven_pos, mystic_pos, screen_reader = get_data()
            extra_coven_bought, extra_mystic_bought = helper.check(
                coven_pos,
                mystic_pos,
                screen_reader,
                bought_coven=coven_bought,
                bought_mystic=mystic_bought,
            )
            coven_bought = coven_bought or extra_coven_bought
            mystic_bought = mystic_bought or extra_mystic_bought

        #Use this as a failsafe to stop before it goes to shit
        if keyboard.is_pressed("q"):
            break

        helper.refresh(refresh_button_pos)

        refresh_count += 1
        print("Refresh Done=", refresh_count)
        print("Spent Skystones=", refresh_count * 3)

    print("You exited successfuly")


if __name__ == "__main__":
    main()
