# https://docs.python.org/2/library/unittest.html
import unittest

from tweet_text import idle_text , reply

# The basic building blocks of unit testing are test cases
# single scenarios that must be set up and checked for correctness.
# In unittest, test cases are represented by instances of unittest's TestCase class.
# To make your own test cases you must write subclasses of TestCase.

<<<<<<< HEAD
class TestTweetText(unittest.TestCase):
	def test_math(self):
		response = reply({'text':'1+1', 'user': {'screen_name': 'TestUser'}})
		self.assertTrue("2" in response)
     #This is called immediately before calling each test method
  # def setUp(self):
        #self.text = idle_text()

    #def test_start(self):
        # In order to test something, we use one of the assert*()
        # methods provided by the TestCase base class
         #https://docs.python.org/2/library/unittest.html#unittest.TestCase.assertTrue
        #self.assertTrue(self.text.startswith('It is'))
=======

class TestTweetText(unittest.TestCase):

    def test_idle(self):
        # In order to test something, we use one of the assert*()
        # methods provided by the TestCase base class
        # https://docs.python.org/2/library/unittest.html#unittest.TestCase.assertTrue
        self.assertTrue( isinstance(idle_text(), str) )

>>>>>>> 04ada90c694c3899890a50bfaaae154fb9b82217


if __name__ == '__main__':
    unittest.main(verbosity=2)
