from common import Common
import time

class ShiLian(object):

    @classmethod
    def shi_lian(cls):
        if Common.thread_nums == 1:
            return
        else:
            Common.thread_nums = 1
        Common.auxiliary_stop = False
        Common.click_image("sl/huodong.png")
        time.sleep(0.5)
        Common.click_image("sl/shilian.png")
        time.sleep(0.5)
        cls.shi_lian_begin()
        time.sleep(0.5)
        Common.click_image("sl/fanghui.png")
        time.sleep(0.5)
        Common.click_image("sl/fanghui.png")
        Common.thread_nums = 0
        
    @classmethod
    def shi_lian_begin(cls):
        while not Common.auxiliary_stop:
            Common.click_image("sl/jiarushilian.png")
            time.sleep(1)
            if Common.find_image("sl/jiarushilian.png"):
                return
            if Common.find_image("sl/shuaxing.png"):
                Common.click_image("sl/tuichu.png")
                time.sleep(0.5)
                Common.click_image("sl/queding.png")
                time.sleep(10)
                Common.click_image("sl/tuichushilian.png")
                time.sleep(0.5)
                Common.click_image("sl/shilian.png")
                time.sleep(0.5)

    @classmethod
    def on_click_shi_lian(cls):
        Common.config_params['shi_lian'] = Common.shi_lian.get()
        Common.save_config_params()
            