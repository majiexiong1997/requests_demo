import unittest


class Test_requests1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_00(self):
        print('测试通过')
    def test_01(self):
        assert 1!=0