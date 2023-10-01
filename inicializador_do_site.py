import pyautogui
import time
import pandas as pd

def inicializando():
    pyautogui.PAUSE = 0.5

    pyautogui.press("win")
    pyautogui.write("Chrome")
    pyautogui.press("enter")

    link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    pyautogui.write(link)
    pyautogui.press("enter")

    # esperando 1seg
    time.sleep(2)

    pyautogui.press("tab")
    pyautogui.write("gabrielnavarro.vip@gmail.com")
    pyautogui.press("tab")
    pyautogui.write("MInhasenhaZinha")
    pyautogui.press("tab")
    pyautogui.press("enter")

    # esperando 1seg
    time.sleep(2)