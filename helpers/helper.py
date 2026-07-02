import time

import mss
import pyautogui
import pytesseract
from PIL import Image

#Focus the game window on import
pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True
screen_size = pyautogui.size()
pyautogui.moveTo(screen_size[0] // 2 + 100, screen_size[1] // 2, duration=0)
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
time.sleep(0.1)
pyautogui.click()
time.sleep(0.1)


def locate(path, confidence):
    try:
        return pyautogui.locateOnScreen(path, confidence=confidence)
    except pyautogui.ImageNotFoundException:
        return None


def read_text() -> str:
    #Read and return all text from the primary monitor
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        image = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
    return pytesseract.image_to_string(image, lang="eng")


def buy(pos, ypos):
    #Click buy on a summon row, then confirm the purchase
    time.sleep(0.3)
    point = pyautogui.center(pos)
    pyautogui.click(
        x=point[0] + 800,
        y=point[1] + ypos,
        clicks=2,
        interval=0.05,
        button="left",
    )
    time.sleep(0.4)
    buy_button = locate("images/ui/buy_button.png", 0.95)
    buy_button_point = pyautogui.center(buy_button)
    pyautogui.click(
        x=buy_button_point[0],
        y=buy_button_point[1],
        clicks=2,
        interval=0.05,
        button="left",
    )


def check(coven_pos, mystic_pos, screen_reader, bought_coven=False, bought_mystic=False):
    #Return a tuple of booleans indicating whether covenant or mystic was bought
    coven_bought = False
    mystic_bought = False

    if not bought_coven:
        if coven_pos is not None:
            print("Buy Covenant Summons.")
            buy(coven_pos, 40)
            coven_bought = True
        elif "covenant" in screen_reader.lower():
            print("Covenant detected by OCR, but covenant position not found.")

    time.sleep(0.1)

    if not bought_mystic:
        if mystic_pos is not None:
            print("Buy Mystic Summons.")
            buy(mystic_pos, 40)
            mystic_bought = True
        elif "mystic" in screen_reader.lower():
            print("Mystic detected by OCR, but mystic position not found.")

    return coven_bought, mystic_bought


def move_screen():
    #Scroll the shop upward to reveal hidden summons
    for _ in range(2):
        x = screen_size[0] // 2 + 300
        pyautogui.moveTo(x, screen_size[1] // 2, duration=0)
        pyautogui.dragTo(x, screen_size[1] // 2 - 300, duration=0.2)
        time.sleep(0.1)


def refresh(refresh_button_pos):
    #Click refresh and confirm the shop reroll
    refresh_point = pyautogui.center(refresh_button_pos)
    pyautogui.click(
        x=refresh_point[0],
        y=refresh_point[1],
        clicks=3,
        interval=0.05,
        button="left",
    )
    #Wait for confirm to appear
    time.sleep(0.5)
    confirm_pos = pyautogui.locateOnScreen(
        "images/ui/confirm_button.PNG", confidence=0.90
    )
    confirm_point = pyautogui.center(confirm_pos)
    time.sleep(0.2)
    pyautogui.click(
        x=confirm_point[0],
        y=confirm_point[1],
        clicks=2,
        interval=0.05,
        button="left",
    )
    #Wait for refresh to complete
    time.sleep(1)