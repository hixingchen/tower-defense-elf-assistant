from common import Common
import time
from task import Task
from xpinyin import Pinyin
import os

class Battle(object):
    @classmethod
    def save(cls):
        Common.config_params['hero_list'] = []
        for entry in Common.hero_entries:
            Common.config_params['hero_list'].append(entry.get())
        Common.save_config_params()

    @classmethod
    def start_battle(cls):
        if Common.thread_nums == 1:
            return
        else:
            Common.thread_nums = 1
        Common.auxiliary_stop = False
        Common.close_chariot()
        for i in range(0,2):
            Common.click_image("gj/yx.png")
            time.sleep(0.5)
            Common.click_image("gj/dz.png")
            time.sleep(0.5)
            Common.click_image("gj/fanhui.png")
            time.sleep(0.5)
        while not Common.auxiliary_stop:
            Common.close_chariot()
            if not Common.find_image("gj/duizhan.png"):
                Common.print_to_text_box(f"未找到对战图片\n")
                Common.click_close()
                time.sleep(2)
                continue
            time.sleep(0.5)
            Common.thread_nums = 0
            Task.do_task()
            Common.thread_nums = 1
            Common.click_image("gj/duizhan.png")
            time.sleep(0.5)
            # 查找并点击快速匹配图片
            found = Common.click_image("gj/kspp.png")
            if not found:
                Common.print_to_text_box(f"未找到快速匹配图片\n")
                time.sleep(2)
                continue
            Common.print_to_text_box(f"已找到快速匹配图片\n")
            time.sleep(0.5)
            while not Common.auxiliary_stop:
                if Common.find_image("gj/shuaxing.png") or Common.find_image("gj/queding.png"):
                    break
                time.sleep(1)
            # 开始选择英雄
            cls.start_game_actions()
            # 看广告
            if Common.find_image("gj/zhenli.png"):
                Common.see_ad("gj/jieshou.png")
            if Common.find_image("gj/biyou.png"):
                if Common.see_failed_ad.get():
                    Common.see_ad("gj/jieshou.png")
                else:
                    Common.click_image("gj/jujue.png")
            time.sleep(2)
        Common.thread_nums = 0
    
    @classmethod
    def start_game_actions(cls):
        while not Common.auxiliary_stop:
            findTemp = False
            if Common.close_chariot():
                break
            if Common.find_image("gj/queding.png"):
                Common.click_image("gj/queding.png")
                time.sleep(2)
                break
            for heroName in Common.config_params['hero_list'][:6]:
                image_filename = Pinyin().get_pinyin(heroName)
                hero_image_path = os.path.join("yx", f"{image_filename}.png")
                findTemp |= Common.click_image(hero_image_path)
                if findTemp:
                    break
            else:
                cls.change_equip()
                for heroName in Common.config_params['hero_list'][6:10]:
                    image_filename = Pinyin().get_pinyin(heroName)
                    hero_image_path = os.path.join("yx", f"{image_filename}.png")
                    findTemp |= Common.click_image(hero_image_path)
                    if findTemp:
                        break
                else:
                    Common.close_chariot()
            if not Common.find_image("gj/kuojian3.png") and findTemp:
                Common.click_image("gj/kuojian.png")
            else:
                Common.click_image("gj/shuaxing.png")
            time.sleep(1)

    @classmethod
    def change_equip(cls):
        if Common.find_image("yx/huan-jing-ling.png"):
            if not Common.find_image("gj/longxing.png",width=Common.target_window.width/2):
                if Common.find_image("gj/qiangxi.png",width=Common.target_window.width/2) or Common.find_image("gj/shengjian.png",width=Common.target_window.width/2) or Common.find_image("gj/yandou.png",width=Common.target_window.width/2):
                    Common.click_image("yx/huan-jing-ling.png")
                    time.sleep(0.5)

    @classmethod
    def on_click_see_failed(cls):
        Common.config_params['see_failed_ad'] = Common.see_failed_ad.get()
        Common.save_config_params()