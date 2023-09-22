from common import Common
import time
from dailySelection import DailySelection
from battle import Battle
from unionDonation import UnionDonation
from cooperate import Cooperate
from shiLian import ShiLian

class OneClickDaily(object):

    @classmethod
    def start_hanging_up(cls):
        if Common.thread_nums == 1:
            return
        else:
            Common.thread_nums = 1
        Common.thread_nums = 0
        # 精选
        DailySelection.buy_hero()
        if Common.auxiliary_stop:
            Common.thread_nums = 0
            return
        else:
            Common.thread_nums = 1
            time.sleep(1)
            Common.thread_nums = 0
        # 联盟捐献
        UnionDonation.donation()
        if Common.auxiliary_stop:
            Common.thread_nums = 0
            return
        else:
            Common.thread_nums = 1
            time.sleep(1)
            Common.thread_nums = 0

        # 试炼
        if Common.shi_lian.get():
            ShiLian.shi_lian()
            if Common.auxiliary_stop:
                Common.thread_nums = 0
                return
            else:
                Common.thread_nums = 1
                time.sleep(1)
                Common.thread_nums = 0

        # 合作
        Cooperate.cooperate_start()
        if Common.auxiliary_stop:
            Common.thread_nums = 0
            return
        else:
            Common.thread_nums = 1
            time.sleep(1)
            Common.thread_nums = 0

        # 对战
        Battle.start_battle()
        if Common.auxiliary_stop:
            Common.thread_nums = 0
            return
        else:
            Common.thread_nums = 1
            time.sleep(1)
            Common.thread_nums = 0
        Common.thread_nums = 0

        