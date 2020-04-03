import  unittest
import random

class TestSeq(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)


     def runTest(self):
         element = random.choice(self.seq)
         self.assertTrue(element in self.seq)



if __name__ == '__main__':
    unittest.main()
