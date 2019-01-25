import time

class earthquakeDataProcessor:
    def __init__(self):
        self.numberAndAverageMagnitudeOfEarthquakesByLocation = {}

    def processCsvRow(self, csvRow):
        if csvRow == None:
            raise ValueError('ERROR: csvRow is required')
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
        if dataProcessor == None:
            raise ValueError('ERROR: dataProcessor is required')
        if dataRows == None:
            raise ValueError('ERROR: dataRows is required')
        self.dataProcessor = dataProcessor
        self.dataRows = dataRows

    def startStreamingData(self):
        for x in range(5):
            row = self.dataRows[x]
            self.dataProcessor.processCsvRow(row)
            time.sleep(2)