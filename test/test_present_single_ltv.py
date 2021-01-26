import os

from presentation import *


def test_present_ltv_across_countries():
    tell_story_about_single_lifetimevalue(9.34)
    os.path.isfile('../OPENME/ltv.png')