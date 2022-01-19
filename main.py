"""
Fer ús d'aquest script li treu la gràcia al joc del Paraulògic (https://vilaweb.cat/paraulogic/)

Script creat per a Biel Martínez i Eric Roy
"""

import pyautogui, time
from requests import get
from json import loads

def escriu():

    s = get("https://vilaweb.cat/paraulogic").text.split("\n")[112]
    s2 = s.split(";")
    t = loads(s2[1].split("=")[1])  #avui

    time.sleep(3)

    for i in t['p']:
        pyautogui.write(i)
        pyautogui.press("enter")


if __name__ == "__main__":
    escriu()