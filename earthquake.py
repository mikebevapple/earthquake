import earthquakeStream
import earthquakeStatic
import earthquakeDataImporter
import unittest

dataImporter = earthquakeDataImporter.csvImporter('./data/1.0_month.csv')
csvData = dataImporter.csvDataRows

calculator = earthquakeStatic.earthquakeCalculator(csvData)
calculator.computeCountsByLocationSource()
calculator.computeAverageMagnitudeByLocationSource()
#calculator.generateDailyHistogramData()
#NOTE: GenerateDailyHistogramData can take an optional timezone argument, as below:
calculator.generateDailyHistogramData('US/Pacific')

processor = earthquakeStream.earthquakeDataProcessor()
simulator = earthquakeStream.earthquakeDataStreamSimulator(processor, csvData)
simulator.startStreamingData()
processor.printAverageMagnitudesByLocationSource()

class streamingAverageTestCase(unittest.TestCase):
    def testStreamingAverageCalculation(self):
        self.assertEqual(earthquakeStream.earthquakeDataProcessor.calculateAverage(3,7.0,4), 4.0)