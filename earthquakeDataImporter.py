import csv

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