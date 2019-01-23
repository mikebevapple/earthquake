import csv

def readCsvIntoDictionary():
    csvData = {}
    numberOfEarthquakesByLocation = {}
    highestEarthquakeCount = 0
    locationWithMostEarthquakes = ()
    with open('./data/1.0_month.csv') as earthquakeData:
        csvReader = csv.DictReader(earthquakeData)
        for row in csvReader:
            location = (row["latitude"], row["longitude"])
            previousEarthquakeCountForLocation = 0
            if location in numberOfEarthquakesByLocation :
                previousEarthquakeCountForLocation = numberOfEarthquakesByLocation.get(location)
            newEarthquakeCountForLocation = previousEarthquakeCountForLocation + 1
            numberOfEarthquakesByLocation[location] = previousEarthquakeCountForLocation
            if highestEarthquakeCount < newEarthquakeCountForLocation :
                highestEarthquakeCount = newEarthquakeCountForLocation
                locationWithMostEarthquakes = location
        print('Location with most earthquakes = {},{} ({})'.format(locationWithMostEarthquakes[0],locationWithMostEarthquakes[1],highestEarthquakeCount))


readCsvIntoDictionary()