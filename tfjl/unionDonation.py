from common import Common
import time

class UnionDonation(object):

    @classmethod
    def donation(cls):
        if Common.thread_nums == 1:
            return
        else:
            Common.thread_nums = 1
        Common.click_image("lm/lianmeng.png")
        time.sleep(0.5)
        Common.click_image("lm/lianmengjuanxian.png")
        time.sleep(0.5)
        Common.see_ad("lm/guanggaojuanxian.png")
        if Common.find_image("lm/guanbi.png"):
            Common.click_image("lm/guanbi.png")
        else:
            Common.click_close()
            Common.click_close()
        for i in range(0,3):
            Common.click_image("lm/lianmengjuanxian.png")
            time.sleep(0.5)
            Common.click_image("lm/zhuanshijuanxian.png")
            time.sleep(0.5)
            Common.click_image("lm/queding.png")
            time.sleep(0.5)
            Common.click_close()
            Common.click_close()
        if Common.find_image("lm/guanbi.png"):
            Common.click_image("lm/guanbi.png")
        time.sleep(0.5)
        Common.click_image("lm/fanhui.png")
        time.sleep(0.5)
        Common.click_image("lm/fanhui.png")
        Common.thread_nums = 0