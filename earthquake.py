import csv

class earthquakeCalculator:
    def __init__(self,path):
        self.csvDataRows = []
        self.readCsv(path)
 
    def readCsv(self, pathToCsv):
        with open(pathToCsv) as earthquakeData:
            csvReader = csv.DictReader(earthquakeData)
            for row in csvReader:
                self.csvDataRows.append(row)
        print('Read {} rows from csv'.format(len(self.csvDataRows)))

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

        for locationEntry, locationValue in numberAndTotalMagnitudeOfEarthquakesByLocation.items():
            print('{} average magnitude = {}'.format(locationEntry, locationValue[1]/locationValue[0]))

obj = earthquakeCalculator('./data/1.0_month.csv')
obj.computeCountsByLocationSource()
obj.computeAverageMagnitudeByLocationSource()