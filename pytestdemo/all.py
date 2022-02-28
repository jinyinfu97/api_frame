import json
import os
import time

import pytest
import requests

from pytestdemo.common.parametrize import read_testcase_yaml

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./temps -o ./reports --clean")



