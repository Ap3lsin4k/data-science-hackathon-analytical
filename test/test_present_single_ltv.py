import os

from presentation import *


def test_present_ltv_across_countries():
    tell_story_about_total_lifetimevalue(9.341)
    os.path.isfile('../OPENME/1) ltv.png')