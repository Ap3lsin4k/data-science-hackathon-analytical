import os
from time import sleep

from categorizer import *




def test_split_data_analytics_by_devices():

    categorize_by_devices("../test/model/categorizer_by_devices.csv")

   # os.isfile
   # sleep(1)
#    os.remove("model/temp/b")