import os

from presentation import *


def test_present_ltv_across_devices():
    present_ltv_compare_between_iphone_and_ipad(15.564, 12.532)
    os.path.isfile('../OPENME/ltv-iphone-ipad.png')