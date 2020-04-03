import unittest

from common.Log import *
from common.base import YzApi


class StartEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = Log()
        cls.r = YzApi()
        cls.r.login()


    @classmethod
    def tearDownClass(cls):
        pass

