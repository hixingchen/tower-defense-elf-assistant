from common import Common
import time

class Task(object):
    @classmethod
    def do_task(cls):
        if Common.thread_nums == 1:
            return
        else:
            Common.thread_nums = 1
        Common.auxiliary_stop = False
        if Common.have_task:
            Common.click_image("gj/renwu.jpg")
            time.sleep(0.5)
            if Common.find_image("gj/renwu.jpg"):
                Common.click_image("gj/renwu.jpg")
        else:
            return
        while not Common.auxiliary_stop:
            time.sleep(1)
            Common.click_position(int(Common.target_window.width/2),int(Common.target_window.height/2))
            time.sleep(1)
            Common.click_position(int(Common.target_window.width/2),int(Common.target_window.height/2))
            time.sleep(0.5)
            if not Common.find_image("gj/baoxiang.png"):
                Common.have_task = False
            else:
                if Common.find_image("gj/lingqubaoxiang.png"):
                    Common.see_ad("gj/lingqubaoxiang.png")
                    continue
            if Common.find_image("gj/lingqujiangli.jpg"):
                Common.click_image("gj/lingqujiangli.jpg")
                time.sleep(0.5)
                Common.see_ad("gj/shuangbeilingqu.png")
                continue
            if Common.auxiliary_stop:
                Common.thread_nums = 0
                return
            break
        Common.click_image("gj/fanhui.png")
        time.sleep(1)
        if not Common.have_task:
            Common.click_image("gj/lingquguangao.png")
            time.sleep(0.5)
            Common.click_position(770,420)
            time.sleep(1)
            Common.click_position(770,420)
            time.sleep(1)
            Common.click_position(770,420)
            time.sleep(0.5)
            Common.click_image("gj/guanbi2.png")
            time.sleep(1)
        Common.thread_nums = 0
