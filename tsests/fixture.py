import unittest


class Test_01(unittest.TestCase):
    def setUp(self):
        print('我是setup')

    def tearDown(self):
        print('我是tearDown')

    def test_one(self):
        print('我是测试方法1')

    def test_two(self):
        print('我是测试方法2')


if __name__ == '__main__':
    unittest.main()
