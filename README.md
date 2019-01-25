# earthquake

This is my submission for the Earthquake Programming Challenge, written in Python (3.7).

The code lives within several modules:
* earthquake.py is the "start here" script that imports and calls the others.
* earthquakeDataImporter contains the csvImporter class, responsible for reading in the csv file
* earthquakeStatic performs calculations on the entire imported dataset
* earthquakeStream processes a row at a time, simulating a data stream model. The earthquakeDataStreamSimulator class within this module feeds a new row to the processor every two seconds for the first five rows, just as an example.

(Questions 1, 2, and 3 are "answered" by earthquakeStatic. Question 4 is "answered" by earthquakeStream.)

The csv file was downloaded on 1/23/19 and is saved in /data.
