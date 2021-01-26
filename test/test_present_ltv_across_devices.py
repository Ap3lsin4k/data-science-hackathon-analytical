import os

from presentation import *


def test_present_ltv_across_devices():
    tell_story_about_lifetimevalue_comparing_devices(15.564, 12.532)
    os.path.isfile('../OPENME/ltv-iphone-ipad.png')