import csv

class CalcAvgAndMedian:
    def calcAvgRatingAndChar(self):
        with open('positiveReviews.csv', errors='ignore') as readFile:
            read_csv = csv.reader(readFile)
            data = list(csv.reader(readFile))

            number_of_rows = len(data)
            number_of_columns = len(data[0])

            sumRate = 0
            sumChar = 0
            for rows in range(1, number_of_rows):
                if data[rows][1] != '':
                    sumRate = sumRate + int(data[rows][1])

                if data[rows][3] != '':
                    sumChar = sumChar + int(data[rows][3])

            avgRate = sumRate/(number_of_rows-1)
            avgChar = sumChar/(number_of_rows-1)

            print("Total positive data points:", number_of_rows-1)
            print("Average rating for positive data points:", avgRate)
            print("Average number of characters of reviews for positive data points:", avgChar)

        with open('negativeReviews.csv', errors='ignore') as readFile:
            read_csv = csv.reader(readFile)
            data = list(csv.reader(readFile))

            number_of_rows = len(data)
            number_of_columns = len(data[0])

            sumRate = 0
            sumChar = 0
            for rows in range(1, number_of_rows):
                if data[rows][1] != '':
                    sumRate = sumRate + int(data[rows][1])

                if data[rows][3] != '':
                    sumChar = sumChar + int(data[rows][3])

            avgRate = sumRate / (number_of_rows - 1)
            avgChar = sumChar / (number_of_rows - 1)

            print("Total negative data points:", number_of_rows - 1)
            print("Average rating for negative data points:", avgRate)
            print("Average number of characters of reviews for negative data points:", avgChar)

    def calcMedianReviewChar(self):
        with open('positiveReviews.csv', errors='ignore') as readFile:
            read_csv = csv.reader(readFile)
            data = list(csv.reader(readFile))

            number_of_rows = len(data)
            number_of_columns = len(data[0])

            charList = []
            for rows in range(1, number_of_rows):
                if data[rows][3] != '':
                    charList.append(int(data[rows][3]))

            sortedCharList = sorted(set(charList))
            dataRows = len(sortedCharList)

            # print(sortedCharList)
            # print(dataRows)

            if (dataRows/2) != 0:
                value = int((dataRows+1)/2)
                medianValue = sortedCharList[value]

            elif dataRows/2 == 0:
                firstValue = sortedCharList(int((dataRows)/2))
                secondValue = sortedCharList((int(dataRows+1)/2))
                medianValue = (firstValue + secondValue)/2

            print("The median value of positive reviews", medianValue)

        with open('negativeReviews.csv', errors='ignore') as readFile:
            read_csv = csv.reader(readFile)
            data = list(csv.reader(readFile))

            number_of_rows = len(data)
            number_of_columns = len(data[0])

            charList = []
            for rows in range(1, number_of_rows):
                if data[rows][3] != '':
                    charList.append(int(data[rows][3]))

            sortedCharList = sorted(set(charList))
            dataRows = len(sortedCharList)

            # print(sortedCharList)
            # print(dataRows)

            if (dataRows / 2) != 0:
                value = int((dataRows + 1) / 2)
                medianValue = sortedCharList[value]

            elif dataRows / 2 == 0:
                firstValue = sortedCharList(int((dataRows) / 2))
                secondValue = sortedCharList((int(dataRows + 1) / 2))
                medianValue = (firstValue + secondValue) / 2

            print("The median value of negative reviews", medianValue)