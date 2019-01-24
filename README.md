# earthquake

This is my submission for the Earthquake Programming Challenge, written in Python (3.7).

The code lives within several modules:
* earthquake.py is the "start here" script module that shows how to import and run the others
* earthquakeDataImporter contains the csvImporter class, responsible for reading from the csv
* earthquakeStatic performs calculations on the entire imported dataset
* earthquakeStream processes a row at a time, simulating a data stream model. The earthquakeDataStreamSimulator class within this module feeds a new row to the processor every two seconds for ten rows.
