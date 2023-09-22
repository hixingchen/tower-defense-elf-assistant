from common import Common
import time
from xpinyin import Pinyin
import os

class HanBing(object):

    hero_list = ['闪','魇','葵','咕咕','小愧','酋长','邪能火炮']

    @classmethod
    def han_bing_start(cls):
        if Common.thread_nums == 1:
            return
        else:
            Common.thread_nums = 1
        Common.auxiliary_stop = False
        for i in range(0,2):
            Common.click_image("gj/yx.png")
            time.sleep(0.5)
            if Common.find_image("gj/yx.png"):
                Common.click_image("gj/yx.png")
                time.sleep(0.5)
            Common.click_image("hb/hanbing.png")
            time.sleep(0.5)
            Common.click_image("gj/fanhui.png")
            time.sleep(0.5)
        Common.click_image("hb/huodong.png")
        while not Common.auxiliary_stop and not Common.find_image("hb/canyu.png"):
            Common.middle_scroll()
            time.sleep(0.2)
        Common.click_image("hb/canyu.png")
        time.sleep(1)
        while not Common.auxiliary_stop and Common.find_image("hb/tiaozhan.png"):
            Common.click_image("hb/tiaozhan.png")
            time.sleep(0.5)
            Common.click_image("hb/yuhaoyouyiqi.png")
            time.sleep(0.5)
            if Common.find_image("hb/chuanjianfanjian.png"):
                Common.click_position(450,430)
            time.sleep(0.5)
            Common.click_image("hb/fengxiang.png")
            time.sleep(5)
            if Common.find_image("hb/guanbi.png"):
                Common.click_image("hb/guanbi.png")
                time.sleep(2)
                if Common.find_image("hb/tiaozhan.png"):
                    continue
            cls.start_game_actions()
            time.sleep(2)
            if Common.find_image("hb/huodong.png"):
                Common.click_image("hb/huodong.png")
                while not Common.auxiliary_stop and not Common.find_image("hb/canyu.png"):
                    Common.middle_scroll()
                    time.sleep(0.2)
                Common.click_image("hb/canyu.png")
                time.sleep(1)
        for i in range(0,2):
            Common.click_image("hb/fanghui.png")
            time.sleep(0.5)
        Common.thread_nums = 0
    
    @classmethod
    def start_game_actions(cls):
        while  not Common.auxiliary_stop :
            if not Common.find_image("hb/shuaxing.png"):
                Common.print_to_text_box(f"未找到刷新按钮")
            else:
                break
            if Common.find_image("hb/queding.png"):
                Common.click_image("hb/queding.png")
                time.sleep(1)
                return
            time.sleep(1)
        time.sleep(2)
        while not Common.auxiliary_stop:
            if Common.find_image("hb/queding.png"):
                Common.click_image("hb/queding.png")
                time.sleep(1)
                return
            for i in range(0,len(cls.hero_list)):
                Common.print_to_text_box(cls.hero_list[i])
                image_filename = Pinyin().get_pinyin(cls.hero_list[i])
                hero_image_path = os.path.join("yx", f"{image_filename}.png")
                Common.print_to_text_box(f"选择英雄中\n")
                if Common.find_image(hero_image_path):
                    Common.click_image(hero_image_path)
                    Common.print_to_text_box(f"点击{hero_image_path}")
                    time.sleep(0.5)
                    if Common.find_image(hero_image_path):
                        Common.click_image("hb/kuojian.png")
            else:
                cls.change_equip()
                if Common.find_image("yx/mu-jing-ling.png"):
                    Common.click_image("yx/mu-jing-ling.png")
                    time.sleep(0.5)
                Common.click_image("hb/shuaxing.png")
            time.sleep(1.5)


    @classmethod
    def change_equip(cls):
        if Common.find_image("yx/huan-jing-ling.png"):
            if not Common.find_image("gj/longxing.png",width=Common.target_window.width/2):
                if Common.find_image("gj/qiangxi.png",width=Common.target_window.width/2) or Common.find_image("gj/shengjian.png",width=Common.target_window.width/2) or Common.find_image("gj/yandou.png",width=Common.target_window.width/2):
                    Common.click_image("yx/huan-jing-ling.png")
                    time.sleep(0.5)