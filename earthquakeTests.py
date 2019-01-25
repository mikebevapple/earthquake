import unittest
import earthquakeStream

class streamingAverageTestCase(unittest.TestCase):
    def testStreamingAverageCalculation(self):
        self.assertEqual(earthquakeStream.earthquakeDataProcessor.calculateAverage(3,7.0,4), 4.0)
