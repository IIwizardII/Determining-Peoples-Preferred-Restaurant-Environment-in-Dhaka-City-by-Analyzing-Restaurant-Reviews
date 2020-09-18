import csv

class SeparateData:
    def dataSeparator(self):
        with open('dataWithAddedFeatures.csv', errors='ignore') as readFile:
            read_csv = csv.reader(readFile)
            data = list(csv.reader(readFile))

            number_of_rows = len(data)
            number_of_columns = len(data[0])

            with open('positiveReviews.csv', 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)

                writer.writerow([data[0][0], data[0][1], data[0][2], "Review Length", "Review Type"])

                for rows in range(1, number_of_rows):
                        if (data[rows][4] == "Positive"):
                            writer.writerow([data[rows][0], data[rows][1], data[rows][2], len(data[rows][0]), "Positive"])

            with open('negativeReviews.csv', 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)

                writer.writerow([data[0][0], data[0][1], data[0][2], "Review Length", "Review Type"])

                for rows in range(1, number_of_rows):
                        if (data[rows][4] == "Negative"):
                            writer.writerow([data[rows][0], data[rows][1], data[rows][2], len(data[rows][0]), "Negative"])
