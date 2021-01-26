import os

from presentation import *


def test_present_ltv_across_countries():
    tell_story_about_lifetimevalue_comparing_countries([100,56,33],['USA','USD','UKR'])
    os.path.isfile('../OPENME/ltv-countries.png')