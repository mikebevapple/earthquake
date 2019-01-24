import csv

class earthquakeCalculator:
    def __init__(self):
        self.numberOfEarthquakesByLocation = {}
        self.csvDataRows = []
 
    def readCsv(self, pathToCsv):
        with open(pathToCsv) as earthquakeData:
            csvReader = csv.DictReader(earthquakeData)
            for row in csvReader:
                self.csvDataRows.append(row)
        print('Read {} rows from csv'.format(len(self.csvDataRows)))

    def computeEarthquakeCounts(self):
        highestEarthquakeCount = 0
        locationWithMostEarthquakes = ()
        multipleLocationsTiedForMostEarthquakes = False

        for row in self.csvDataRows:
            locationSource = row["locationSource"]
            previousEarthquakeCountForLocation = 0
            if locationSource in self.numberOfEarthquakesByLocation :
                previousEarthquakeCountForLocation = self.numberOfEarthquakesByLocation.get(locationSource)
            newEarthquakeCountForLocation = previousEarthquakeCountForLocation + 1
            self.numberOfEarthquakesByLocation[locationSource] = newEarthquakeCountForLocation
            if highestEarthquakeCount < newEarthquakeCountForLocation :
                highestEarthquakeCount = newEarthquakeCountForLocation
                locationWithMostEarthquakes = locationSource
                multipleLocationsTiedForMostEarthquakes = False
            elif highestEarthquakeCount == newEarthquakeCountForLocation :
                multipleLocationsTiedForMostEarthquakes = True

        print('Location with most earthquakes ({}) = {}'.format(highestEarthquakeCount,locationWithMostEarthquakes))
        if multipleLocationsTiedForMostEarthquakes :
            print("*More than one location tied for most earthquakes")

obj = earthquakeCalculator()
obj.readCsv('./data/1.0_month.csv')
obj.computeEarthquakeCounts()