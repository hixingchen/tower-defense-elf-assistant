from pygetwindow import *
from common import Common
from tkinter import messagebox

class Positioning(object):
    # 初始化窗口位置
    @classmethod
    def preparation(cls):
        try:
            Common.target_window = getWindowsWithTitle(Common.window_title)[0]
            Common.target_window.moveTo(0, 0)
            Common.root.update()
            Common.root.geometry(f'+0+{Common.target_window.height}')
            Common.print_to_text_box(f"运行成功，请确保{Common.window_title}已经移动到左上角\n")
        except IndexError:
            messagebox.showerror(title="错误", message="找不到{Common.window_title}窗口，请确保它已打开。")