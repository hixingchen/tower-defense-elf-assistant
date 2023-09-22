from tkinter import *
import yaml
from pynput import keyboard
import threading
from battle import Battle
from common import Common
from positioning import Positioning
from task import Task
from cooperate import Cooperate
from unionDonation import UnionDonation
from dailySelection import DailySelection
from oneClickDaily import OneClickDaily
from shiLian import ShiLian
from hanbing import HanBing

class Main(object):
    @classmethod
    def on_closing(cls):
        Common.auxiliary_stop = True
        Common.listener.stop()
        Common.root.destroy()
    @classmethod
    def key_press(cls,key):
        if str(key) == 'Key.esc':
            Common.auxiliary_stop = True
    @classmethod
    def key_release(cls,key):
        pass

    # 键盘监听
    @classmethod
    def listenKeyboard(cls):
        Common.listener = keyboard.Listener(on_press=cls.key_press,on_release=cls.key_release)
        Common.listener.run()
    @classmethod
    def MyThread(cls,func, *args):
        '''将函数打包进线程'''
        # 创建
        t = threading.Thread(target=func, args=args) 
        # 守护 !!!
        t.setDaemon = True
        # 启动
        t.start()
        # 阻塞--卡死界面！
        # t.join()

    # 生成界面
    @classmethod
    def start(cls):
        Common.root = Tk()
        Common.see_failed_ad = BooleanVar()
        Common.shi_lian = BooleanVar()
        with open('config.yml','r') as file:
            try:
                Common.config_params = yaml.safe_load(file)
                Common.see_failed_ad.set(Common.config_params['see_failed_ad'])
                Common.shi_lian.set(Common.config_params['shi_lian'])
            except:
                print(f"读取配置文件出错")
        Common.root.protocol("WM_DELETE_WINDOW", cls.on_closing)# 监听辅助关闭事件
        Common.root.title("塔防助手")
        frame = Frame(Common.root)
        frame.pack(padx=10,pady=10)
        # 创建英雄输入框
        heroLabel = Label(frame,text="对战权重:")
        heroLabel.grid(row=2, column=0, padx=5)
        for i in range(10):
            entryTemp = Entry(frame,width=5)
            entryTemp.grid(row=2,column=i+1,padx=5)
            Common.hero_entries.append(entryTemp)
        for i, hero_name in enumerate(Common.config_params['hero_list'][:10]):
            Common.hero_entries[i].insert(0, hero_name)
        save_button = Button(frame, text="保存权重", bg="green",fg='#ffffff', command=lambda :cls.MyThread(Battle.save))
        save_button.grid(row=2, column=11, padx=10,pady=5)
        Common.text_box = Text(frame, height=20, width=80)
        Common.text_box.grid(row=4, column=0, columnspan=10, padx=5, pady=5)

        position_button = Button(frame, text="定位", command=Positioning.preparation)
        position_button.grid(row=1, column=0, padx=5, pady=5)

        battle_button = Button(frame, text="对战", command=lambda :cls.MyThread(Battle.start_battle))
        battle_button.grid(row=1, column=1, padx=5, pady=5)

        ad_check = Checkbutton(frame,text="庇佑",variable=Common.see_failed_ad,onvalue=True,offvalue=False,command=lambda :cls.MyThread(Battle.on_click_see_failed))
        ad_check.grid(row=1,column=2,padx=5,pady=5)

        task_button = Button(frame, text="任务", command=lambda :cls.MyThread(Task.do_task))
        task_button.grid(row=1, column=3, padx=5, pady=5)

        stop_button = Button(frame, text="停止(ESC)", command=lambda :cls.MyThread(Common.stop))
        stop_button.grid(row=1, column=4, padx=5, pady=5)
        # stop_button.grid(row=1, column=4, padx=5, pady=5,columnspan=2) 横跨2格

        cooperate_button = Button(frame, text="合作", command=lambda :cls.MyThread(Cooperate.cooperate_start))
        cooperate_button.grid(row=1, column=5, padx=5, pady=5)

        unionDonation_button = Button(frame, text="捐献",command=lambda :cls.MyThread(UnionDonation.donation))
        unionDonation_button.grid(row=1,column=6,padx=5,pady=5)

        dailySelection_button = Button(frame, text="精选",command=lambda :cls.MyThread(DailySelection.buy_hero))
        dailySelection_button.grid(row=1,column=7,padx=5,pady=5)

        shiLian_check = Checkbutton(frame,text="试炼",variable=Common.shi_lian,onvalue=True,offvalue=False,command=lambda :cls.MyThread(ShiLian.on_click_shi_lian))
        shiLian_check.grid(row=1,column=8,padx=5,pady=5)

        hangbing_button = Button(frame,text="寒冰",command=lambda :cls.MyThread(HanBing.han_bing_start))
        hangbing_button.grid(row=1,column=9,padx=5,pady=5)

        oneClickDaily_button = Button(frame,text="一键日常",command=lambda :cls.MyThread(OneClickDaily.start_hanging_up))
        oneClickDaily_button.grid(row=1,column=10,padx=5,pady=5,columnspan=2)
        
        # test_button = Button(frame,text="位置",command=lambda :cls.MyThread(Common.get_mouse_position))
        # test_button.grid(row=1,column=10,padx=5,pady=5)

        cls.MyThread(cls.listenKeyboard)

        Common.root.mainloop()


if __name__ == "__main__":
    Main.start()