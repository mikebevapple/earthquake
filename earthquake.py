import csv

def readCsvIntoDictionary():
    csvData = {}
    numberOfEarthquakesByLocation = {}
    highestEarthquakeCount = 0
    locationWithMostEarthquakes = ()
    multipleLocationsTiedForMostEarthquakes = False
    with open('./data/1.0_month.csv') as earthquakeData:
        csvReader = csv.DictReader(earthquakeData)
        for row in csvReader:
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

readCsvIntoDictionary()