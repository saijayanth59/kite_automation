import pyautogui as pg
from time import sleep
import pandas as pd
import pyperclip

pyperclip.set_clipboard("xclip")


def cord(x, y):
    return x * 1366, y * 768


def go_zoom_in():
    pg.moveTo(cord(0.475, 0.85))


def go_zoom_out():
    pg.moveTo(cord(0.449, 0.85))


def go_table_view():
    pg.moveTo(cord(0.868, 0.035))


def zoomout():
    pg.press("subtract")


def zoomin():
    pg.press("add")


def to_copy_btn():
    pg.moveTo(cord(0.12, 0.11))


def to_download_btn():
    pg.moveTo(cord(0.19, 0.11))


def to_additional_columns_btn():
    pg.moveTo(cord(0.3, 0.11))


def escape():
    pg.press("esc")


def left_slide():
    pg.hotkey("alt", "left")


def click(t=0.5):
    sleep(t)
    pg.click()


def main():
    sleep(2)

    data = None
    for _ in range(25):
        zoomout()
    for _ in range(2):
        go_table_view()
        click()
        to_copy_btn()
        click(t=1)
        if data is None:
            data = pd.read_clipboard()
        else:
            data = pd.concat([data, pd.read_clipboard()],
                             axis=0).drop_duplicates()
        escape()
        sleep(1)
        left_slide()
        sleep(1)

    data.to_csv("data.csv")


main()
