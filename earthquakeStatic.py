from dateutil.parser import *
from datetime import datetime
from pytz import timezone
import pytz

class earthquakeCalculator:
    def __init__(self,dataRows):
        if dataRows == None:
            raise ValueError('ERROR: dataRows is required')
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
            print('Unsupported Timezone string, using UTC')

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