import csv

def readCsvIntoDictionary():
    csv_data = {}
    location_earthquake_count = {}
    highest_earthquake_count = 0
    highest_earthquake_location = ()
    with open('./data/1.0_month.csv') as earthquake_data:
        csv_reader = csv.DictReader(earthquake_data)
        for row in csv_reader:
            location = (row["latitude"], row["longitude"])
            previous_earthquake_count_for_location = 0
            if location in location_earthquake_count :
                previous_earthquake_count_for_location = location_earthquake_count.get(location)
            new_earthquake_count_for_location = previous_earthquake_count_for_location + 1
            location_earthquake_count[location] = previous_earthquake_count_for_location
            if highest_earthquake_count < new_earthquake_count_for_location :
                highest_earthquake_count = new_earthquake_count_for_location
                highest_earthquake_location = location
        print('Location with most earthquakes = {},{} ({})'.format(highest_earthquake_location[0],highest_earthquake_location[1],highest_earthquake_count))


readCsvIntoDictionary()