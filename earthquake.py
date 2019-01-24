import csv
from dateutil.parser import *
from datetime import datetime
from pytz import timezone
import pytz
import time

class csvImporter:
    def __init__(self, path):
        self.csvDataRows = []
        self.readCsv(path)

    def readCsv(self, pathToCsv):
        with open(pathToCsv) as earthquakeData:
            csvReader = csv.DictReader(earthquakeData)
            for row in csvReader:
                self.csvDataRows.append(row)
        print('Read {} rows from csv'.format(len(self.csvDataRows)))
        print('-----------')

class earthquakeCalculator:
    def __init__(self,dataRows):
        self.csvDataRows = dataRows

    def computeCountsByLocationSource(self):
        numberOfEarthquakesByLocation = {}
        highestEarthquakeCount = 0
        locationWithMostEarthquakes = ()
        multipleLocationsTiedForMostEarthquakes = False

        for row in self.csvDataRows:
            locationSource = row["locationSource"]
            previousEarthquakeCountForLocation = 0
            if locationSource in numberOfEarthquakesByLocation :
                previousEarthquakeCountForLocation = numberOfEarthquakesByLocation.get(locationSource)
            newEarthquakeCountForLocation = previousEarthquakeCountForLocation + 1
            numberOfEarthquakesByLocation[locationSource] = newEarthquakeCountForLocation
            if highestEarthquakeCount < newEarthquakeCountForLocation :
                highestEarthquakeCount = newEarthquakeCountForLocation
                locationWithMostEarthquakes = locationSource
                multipleLocationsTiedForMostEarthquakes = False
            elif highestEarthquakeCount == newEarthquakeCountForLocation :
                multipleLocationsTiedForMostEarthquakes = True

        print('Location with most earthquakes ({}) = {}'.format(highestEarthquakeCount,locationWithMostEarthquakes))
        if multipleLocationsTiedForMostEarthquakes :
            print("*More than one location tied for most earthquakes")
        print('-----------')

    def computeAverageMagnitudeByLocationSource(self):
        numberAndTotalMagnitudeOfEarthquakesByLocation = {}

        for row in self.csvDataRows:
            locationSource = row['locationSource']
            rowMagnitude = float(row['mag'])
            previousEarthquakeCountForLocation = 0
            previousTotalMagnitudeForLocation = 0
            if locationSource in numberAndTotalMagnitudeOfEarthquakesByLocation :
                existingRecordForLocation = numberAndTotalMagnitudeOfEarthquakesByLocation.get(locationSource)
                previousEarthquakeCountForLocation = existingRecordForLocation[0]
                previousTotalMagnitudeForLocation = existingRecordForLocation[1]
            newEarthquakeCountForLocation = previousEarthquakeCountForLocation + 1
            newTotalMagnitudeForLocation = previousTotalMagnitudeForLocation + rowMagnitude
            numberAndTotalMagnitudeOfEarthquakesByLocation[locationSource] = (newEarthquakeCountForLocation,newTotalMagnitudeForLocation)

        for locationKey, locationValue in numberAndTotalMagnitudeOfEarthquakesByLocation.items():
            print('{} average magnitude = {}'.format(locationKey, locationValue[1]/locationValue[0]))
        print('-----------')

    def generateDailyHistogramData(self, timezoneString='UTC'):
        numberOfEarthquakesPerDay = {}
        timeZoneToUse = pytz.utc

        try:
            timeZoneToUse = timezone(timezoneString)
        except UnknownTimeZoneError:
            print('Unsupported Timezone string')

        for row in self.csvDataRows:
            datetime = parse(row['time'])
            localizedDateTime = datetime.astimezone(timeZoneToUse)
            timeZoneDate = localizedDateTime.date()
            previousEarthquakeCountForDate = 0
            if timeZoneDate in numberOfEarthquakesPerDay :
                previousEarthquakeCountForDate = numberOfEarthquakesPerDay.get(timeZoneDate)
            newEarthquakeCountForDate = previousEarthquakeCountForDate + 1
            numberOfEarthquakesPerDay[timeZoneDate] = newEarthquakeCountForDate

        for date, numberOfEarthquakes in numberOfEarthquakesPerDay.items():
            print('{} total earthquakes = {}'.format(date, numberOfEarthquakes))
        print('-----------')

class earthquakeDataProcessor:
    def __init__(self):
        self.numberAndAverageMagnitudeOfEarthquakesByLocation = {}

    def processCsvRow(self, csvRow):
        locationSource = csvRow['locationSource']
        rowMagnitude = float(csvRow['mag'])
        previousEarthquakeCountForLocation = 0
        previousAverageMagnitudeForLocation = 0
        if locationSource in self.numberAndAverageMagnitudeOfEarthquakesByLocation :
            existingRecordForLocation = self.numberAndAverageMagnitudeOfEarthquakesByLocation.get(locationSource)
            previousEarthquakeCountForLocation = existingRecordForLocation[0]
            previousAverageMagnitudeForLocation = existingRecordForLocation[1]
        newEarthquakeCountForLocation = previousEarthquakeCountForLocation + 1
        newAverageMagnitudeForLocation = previousAverageMagnitudeForLocation + (rowMagnitude - previousAverageMagnitudeForLocation) / newEarthquakeCountForLocation        
        self.numberAndAverageMagnitudeOfEarthquakesByLocation[locationSource] = (newEarthquakeCountForLocation,newAverageMagnitudeForLocation)
        print('Processed row: location {}, magnitude {}'.format(locationSource, rowMagnitude))

    def printAverageMagnitudesByLocationSource(self):
        for locationKey, locationValue in self.numberAndAverageMagnitudeOfEarthquakesByLocation.items():
            print('{} average magnitude = {}'.format(locationKey, locationValue[1]))
        print('-----------')

class earthquakeDataStreamSimulator:
    def __init__(self, dataProcessor, dataRows):
        self.dataProcessor = dataProcessor
        self.dataRows = dataRows

    def startStreamingData(self):
        for x in range(5):
            row = self.dataRows[x]
            self.dataProcessor.processCsvRow(row)
            time.sleep(2)

dataImporter = csvImporter('./data/1.0_month.csv')
csvData = dataImporter.csvDataRows

calculator = earthquakeCalculator(csvData)
calculator.computeCountsByLocationSource()
calculator.computeAverageMagnitudeByLocationSource()
calculator.generateDailyHistogramData()
#NOTE: GenerateDailyHistogramData can take an optional timezone argument, as below:
#calculator.generateDailyHistogramData('US/Pacific')

processor = earthquakeDataProcessor()
simulator = earthquakeDataStreamSimulator(processor, csvData)
simulator.startStreamingData()
processor.printAverageMagnitudesByLocationSource()