import csv

class csvImporter:
    def __init__(self, path):
        if path == None:
            raise ValueError('ERROR: path is required')
        self.csvDataRows = []
        self.readCsv(path)

    def readCsv(self, pathToCsv):
        try:
            with open(pathToCsv) as earthquakeData:
                csvReader = csv.DictReader(earthquakeData)
                for row in csvReader:
                    self.csvDataRows.append(row)
            print('Read {} rows from csv'.format(len(self.csvDataRows)))
            print('-----------')
        except OSError:
            print('ERROR: could not read CSV file from disk. Please check that your path is a valid CSV.')