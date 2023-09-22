from common import Common
import time
import os

class DailySelection(object):
    
    @classmethod
    def buy_hero(cls):
        if Common.thread_nums == 1:
            return
        else:
            Common.thread_nums = 1
        Common.auxiliary_stop = False
        heros = os.listdir('jx/yx')
        if Common.find_image("jx/shandian.png"):
            Common.click_image("jx/shandian.png")
        else:
            return
        while not Common.auxiliary_stop and not Common.find_image("jx/meirijingxuan.png",Common.target_window.width*0.5):
            Common.middle_scroll()
            time.sleep(0.2)
        
        while not Common.auxiliary_stop:
            # 领取免费英雄
            if Common.find_image("jx/mianfeilingqu.png"):
                Common.click_image("jx/mianfeilingqu.png")
                time.sleep(0.5)
                Common.click_close()
                time.sleep(0.5)
                Common.click_close()
            # 购买需要的英雄
            for hero in heros:
                if Common.find_image("jx/yx/"+hero):
                    Common.click_image("jx/yx/"+hero)
                    time.sleep(0.5)
                    Common.click_image("jx/buy.png")
                    time.sleep(0.5)
                    if Common.find_image("jx/guanbi.png"):
                        Common.click_image("jx/guanbi.png")
                        time.sleep(0.5)
                        Common.click_image("jx/fanhui.png")
                        Common.thread_nums = 0
                        return
                    else:
                        Common.click_close()
                        time.sleep(0.5)
                        Common.click_close()
            time.sleep(0.5)
            Common.click_image("jx/shuaxing.png")
            time.sleep(0.5)
            if not Common.find_image("jx/lijishuaxing.png") or Common.auxiliary_stop:
                Common.click_image("jx/fanhui.png")
                Common.thread_nums = 0
                return
            Common.see_ad("jx/lijishuaxing.png")
            time.sleep(10)
        Common.thread_nums = 0
                