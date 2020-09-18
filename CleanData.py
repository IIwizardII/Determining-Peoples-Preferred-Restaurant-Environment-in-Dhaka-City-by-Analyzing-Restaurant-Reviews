import pandas as pd
import csv

class ReadData:
    def loadDataAndClean(self):
        with open('data.csv', errors='ignore') as readFile:
            read_csv = csv.reader(readFile)
            data = list(csv.reader(readFile))

            number_of_rows = len(data)
            number_of_columns = len(data[0])

            with open('cleanedData.csv', 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)

                for rows in range(number_of_rows):
                        if data[rows][1] != '' or data[rows][2] != '':
                            writer.writerow([data[rows][0], data[rows][1], data[rows][2]])