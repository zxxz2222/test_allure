import unittest

case_dir = '../tsests/'
discover = unittest.defaultTestLoader.discover(case_dir,pattern='softtest*.py')
unittest.TextTestRunner().run(discover)