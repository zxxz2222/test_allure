import unittest
from tsests.test01 import One


suite = unittest.TestSuite()
suite.addTest(One('test01'))
suite.addTest(One('test02'))


runner = unittest.TextTestRunner()
runner.run(suite)

if __name__ == '__main__':
    unittest.main()
