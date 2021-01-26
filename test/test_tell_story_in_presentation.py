import os

import pytest

from presentation import *



@pytest.mark.skip("confusing with plots based on real data")
def test_present_ltv_across_countries():
    tell_story_about_lifetimevalue_comparing_countries([100,56,33],['USA','USD','UKR'])
    os.path.isfile('../OPENME/ltv-countries.png')

@pytest.mark.skip("confusing with plots based on real data")
def test_present_ltv_across_devices():
    tell_story_about_lifetimevalue_comparing_devices(15.564, 12.532)
    os.path.isfile('../OPENME/ltv-iphone-ipad.png')
