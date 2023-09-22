import pyautogui
import cv2
import numpy as np
from tkinter import *
from pygetwindow import *
import yaml
import win32api,win32con
import time

class Common(object):
    text_box  = None
    root = None # 根界面
    target_window = None # 目标窗口
    auxiliary_stop = False # 是否停止游戏
    window_title = '塔防精灵'
    listener = '' # 监听键盘
    hero_entries = [] # 对战英雄集
    have_task = True # 是否有任务
    see_failed_ad = None # 是否看失败广告
    shi_lian = None # 是否参加试炼
    config_params = {
        'hero_list':[], # 英雄列表
        'see_failed_ad':True, # 是否看失败广告
        'shi_lian':True # 是否参加试炼
    }
    thread_nums = 0 # 线程数量
    @classmethod
    def click_image(cls,image_path,width=0,height=0,conf=0.8):
        try:
            if width == 0:
                width = cls.target_window.width
            if height == 0:
                height = cls.target_window.height
        except:
            Common.auxiliary_stop = True
            cls.print_to_text_box("请先定位")
            return False
        screenshot = pyautogui.screenshot(region=(0,0,width,height))
        img_rgb = np.array(screenshot)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(image_path, 0)
        if template.shape[0] > img_gray.shape[0] or template.shape[1] > img_gray.shape[1]:
            cls.print_to_text_box(f"模板图像尺寸大于截屏图像尺寸，跳过匹配操作。\n")
            return False
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= conf)

        if len(loc[0]) > 0:
            cls.print_to_text_box(f"找到 {image_path} 图片！\n")
            y, x = loc[0][0], loc[1][0]
            center = (x + template.shape[1] // 2, y + template.shape[0] // 2)
            try:
                window = getWindowsWithTitle(cls.window_title)[0]
                x_offset, y_offset = window.topleft
                center = (x_offset + x + template.shape[1] // 2, y_offset + y + template.shape[0] // 2)
            except IndexError:
                pass
            cls.click_position(int(center[0]),int(center[1]))
            cls.print_to_text_box(f"点击成功：{image_path}\n")
            return True
        else:
            cls.print_to_text_box(f"未找到 {image_path} 图片。\n")
            return False
        
    @classmethod
    def find_image(cls,image_path,width=0,height=0,conf=0.8):
        try:
            if width == 0:
                width = cls.target_window.width
            if height == 0:
                height = cls.target_window.height
        except:
            Common.auxiliary_stop = True
            cls.print_to_text_box("请先定位")
            return False
        cls.text_box.insert(END, f"正在查找 {image_path} 图片...\n")
        cls.text_box.see(END)
        screenshot = pyautogui.screenshot(region=(0,0,width,height))
        img_rgb = np.array(screenshot)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        template = cv2.imread(image_path, 0)
        if template.shape[0] > img_gray.shape[0] or template.shape[1] > img_gray.shape[1]:
            cls.print_to_text_box(f"模板图像尺寸大于截屏图像尺寸，跳过匹配操作。\n")
            return False
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= conf)

        if len(loc[0]) > 0:
            cls.print_to_text_box(f"找到 {image_path} 图片！\n")
            return True
        else:
            cls.print_to_text_box(f"未找到 {image_path} 图片。\n")
            return False

    @classmethod
    def print_to_text_box(cls,text):
        cls.text_box.insert(END, text)
        cls.text_box.see(END)
    
    @classmethod
    def save_config_params(cls):
        with open('config.yml','w') as file:
            yaml.dump(cls.config_params,file)
    
    @classmethod
    def click_position(cls,x,y):
        tempX,tempY = win32api.GetCursorPos()
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        win32api.SetCursorPos((tempX,tempY))

    # 打印鼠标位置
    @classmethod
    def get_mouse_position(cls):
        while not cls.auxiliary_stop:
            x,y = pyautogui.position()
            print(x,y)
            time.sleep(1)

    @classmethod
    def middle_scroll(cls):
        win32api.SetCursorPos((200,200))
        pyautogui.scroll(1000)

    @classmethod
    def close_chariot(cls):# 关闭战车界面
        if cls.find_image("gj/zhanche.png") or cls.find_image("gj/jujue.png"):
            cls.click_image("gj/guanbi2.png")
            cls.click_image("gj/jujue.png")
            return True
        
    @classmethod
    def click_close(cls):
        cls.click_position(990,75)

    #看广告
    @classmethod
    def see_ad(cls,path):
        cls.click_image(path)
        time.sleep(0.5)
        if cls.find_image("gj/quxiao.png"):
            cls.click_image("gj/quxiao.png")
        for i in range(0,35):
            time.sleep(1)
            if cls.auxiliary_stop:
                break
        if not cls.click_image("gj/guanbi.png"):
            cls.click_close()
        time.sleep(1)
        return True

    # 停止辅助
    @classmethod
    def stop(cls):
        cls.auxiliary_stop = True