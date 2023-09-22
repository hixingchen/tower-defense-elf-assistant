from common import Common
import time
from xpinyin import Pinyin
import os

class Cooperate(object):

    hero_list = ['冰法','地精','地精宝库','酋长','飞机','女妖','悟空']
    hero_level = [0,0,0,0,0,0,0]
    hero_target_level = [4,4,4,4,4,4,1]
    hero_temp = []
    left_positions = [[143,446],[108,446],[143,375],[108,375],[143,303],[108,303]]
    right_positions = [[272,446],[239,446],[272,374],[239,374],[272,301],[239,301]]
    di_jing_index = 0
    wu_kong_index = 0
    flag = False #是否过300，过300就退出合作

    @classmethod
    def cooperate_start(cls):
        if Common.thread_nums == 1:
            return
        else:
            Common.thread_nums = 1
        Common.auxiliary_stop = False
        Common.close_chariot()
        for i in range(0,2):
            Common.click_image("gj/yx.png")
            time.sleep(0.5)
            if Common.find_image("gj/yx.png"):
                Common.click_image("gj/yx.png")
                time.sleep(0.5)
            Common.click_image("gj/hz.png")
            time.sleep(0.5)
            Common.click_image("gj/fanhui.png")
            time.sleep(0.5)
        while not Common.auxiliary_stop and (Common.find_image("hz/hezuo.png") or Common.find_image("hz/hezuocishu.png")):
            if Common.find_image("hz/hezuocishu.png"):
                Common.click_image("hz/hezuocishu.png")
                time.sleep(0.5)
                Common.see_ad("hz/guankan.png")
                continue
            cls.hero_level = [0,0,0,0,0,0,0]
            cls.hero_temp = []
            cls.di_jing_index = 0
            cls.wu_kong_index = 0
            Common.click_image("hz/hezuo.png")
            time.sleep(0.5)
            Common.click_image("hz/yuhaoyouyiqi.png")
            time.sleep(0.5)
            if Common.find_image("hz/chuanjianfanjian.png"):
                Common.click_position(450,430)
            time.sleep(0.5)
            Common.click_image("hz/fenxiang.png")
            time.sleep(1)
            if Common.find_image("hz/guanbi.png"):
                Common.click_image("hz/guanbi.png")
                time.sleep(2)
                if Common.find_image("hz/hezuo.png"):
                    continue
            cls.start_game_actions()
            time.sleep(2)
            if cls.flag:
                break
        Common.thread_nums = 0

    @classmethod
    def start_game_actions(cls):
        while  not Common.auxiliary_stop :
            if not Common.find_image("hz/shuaxing.png"):
                Common.print_to_text_box(f"未找到刷新按钮")
            else:
                break
            if Common.find_image("hz/queding.png"):
                Common.click_image("hz/queding.png")
                time.sleep(1)
                return
            time.sleep(1)
        time.sleep(2)

        while not Common.auxiliary_stop:
            if Common.find_image("hz/queding.png"):
                Common.click_image("hz/queding.png")
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
                    if not Common.find_image(hero_image_path):
                        if cls.hero_list[i] != '地精宝库' and cls.hero_level[i] == 0:
                            cls.hero_temp.append(cls.hero_list[i])
                        cls.hero_level[i] += 1
                        pass
                    else:
                        Common.click_image("hz/kuojian.png")
                    break
            else:
                Common.click_image("hz/shuaxing.png")
            time.sleep(1.5)
            temp = True
            for i in range(0,len(cls.hero_target_level)):
                if cls.hero_target_level[i]>cls.hero_level[i]:
                    temp = False
                    break
            if temp:
                break
        cls.wu_kong_index = cls.hero_temp.index('悟空')
        cls.di_jing_index = cls.hero_temp.index('地精')
        positions = []
        Common.click_position(cls.left_positions[0][0],cls.left_positions[0][1])
        time.sleep(0.5)
        if Common.find_image("hz/shanchu.png"):
            positions = cls.left_positions # 自己战车在左边
        else:
            positions = cls.right_positions # 自己战车在右边
        time.sleep(0.5)
        Common.click_image("hz/guanbi.png")

        # 判断是否有电法，如果没有就把牛头换成电法
        for i in range(0,10):
            if Common.find_image("hz/dianfa.png"):
                break
            if Common.find_image("hz/queding.png") or Common.auxiliary_stop:
                Common.click_image("hz/queding.png")
                time.sleep(1)
                return
            time.sleep(1)
        else:
            qiu_zhang_index = cls.hero_temp.index('酋长')
            Common.click_position(positions[qiu_zhang_index][0],positions[qiu_zhang_index][1])
            time.sleep(0.5)
            Common.click_image("hz/shanchu.png")
            time.sleep(0.5)
            dianfa_nums = 0
            while not Common.auxiliary_stop:
                if Common.find_image("hz/queding.png"):
                    Common.click_image("hz/queding.png")
                    time.sleep(1)
                    return
                if Common.find_image("yx/dian-fa.png"):
                    Common.click_image("yx/dian-fa.png")
                    dianfa_nums +=1
                    time.sleep(0.5)
                else:
                    Common.click_image("hz/shuaxing.png")
                    time.sleep(1.5)
                if dianfa_nums >= 4:
                    break

        # 卖掉地精和猴子
        while not Common.auxiliary_stop:
            if Common.find_image("hz/queding.png"):
                Common.click_image("hz/queding.png")
                time.sleep(1)
                return
            if Common.find_image("hz/nvwang.png"):
                Common.click_position(positions[cls.di_jing_index][0],positions[cls.di_jing_index][1])
                time.sleep(0.5)
                Common.click_image("hz/shanchu.png")
                time.sleep(0.5)
                Common.click_position(positions[cls.wu_kong_index][0],positions[cls.wu_kong_index][1])
                time.sleep(0.5)
                Common.click_image("hz/shanchu.png")
                break
            else:
                time.sleep(2)

        gong_jiang_num = 0
        yan_mo_num = 0
        # 上工匠和阎魔
        while not Common.auxiliary_stop:
            if Common.find_image("hz/queding.png"):
                Common.click_image("hz/queding.png")
                time.sleep(1)
                return
            if Common.find_image("yx/gong-jiang.png") and gong_jiang_num < 4:
                Common.click_image("yx/gong-jiang.png")
                gong_jiang_num += 1
            elif Common.find_image("yx/yan-mo.png") and yan_mo_num < 3:
                Common.click_image("yx/yan-mo.png")
                yan_mo_num += 1
            Common.click_image("hz/shuaxing.png")
            time.sleep(1.5)
            if gong_jiang_num == 4 and yan_mo_num >=1:
                break
        
        # 等待退出
        while not Common.auxiliary_stop:
            if Common.find_image("hz/boss-310.png"):
                cls.flag = True
            if Common.find_image("hz/queding.png"):
                Common.click_image("hz/queding.png")
                time.sleep(1)
                return
            # 丢魔精灵
            # if Common.find_image("hz/boss-300.png"):
            #     if Common.find_image("yx/mo-jing-ling.png"):
            #         Common.click_image("yx/mo-jing-ling.png")
            #     else:
            #         Common.click_image("hz/shuaxing.png")
            time.sleep(3)
