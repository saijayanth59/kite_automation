import pyautogui as pg
from time import sleep
import pandas as pd


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


def click(t=1, image=None):
    sleep(t)
    if image:
        pg.click(image)
    else:
        pg.click()


def main():
    sleep(2)

    for _ in range(25):
        zoomout()
    for _ in range(1):
        go_table_view()
        click()
        click(image="download.png")
        sleep(2)
        escape()
        left_slide()
        sleep(2)


main()
