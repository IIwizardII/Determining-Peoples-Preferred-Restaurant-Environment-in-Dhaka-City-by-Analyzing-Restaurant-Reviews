import csv

class DataAnalysis:
    def getMainKeyWordFrequency(self):

        mainKeyWords = ["Food", "Decoration", "Music", "Behavior", "Hospitality", "Waiter", "Staff",
                        "Service", "Taste", "Environment", "Price", "Cost", "Place"]

        with open('positiveReviews.csv', errors='ignore') as readFile:
            read_csv = csv.reader(readFile)
            data = list(csv.reader(readFile))

            number_of_rows = len(data)
            number_of_columns = len(data[0])
            searchSpace = []

            for rows in range(1, number_of_rows):
                searchSpace.append(data[rows][0])

            searchSpaceRows = len(searchSpace)

            countMainKeyWords = dict()

            for rows in range(0, searchSpaceRows):
                for key in mainKeyWords:
                    if str(searchSpace[rows]).lower().find(str(key).lower()) != -1:
                        if key in countMainKeyWords:
                            countMainKeyWords[str(key)] += 1
                        else:
                            countMainKeyWords[key] = 1

            for key in mainKeyWords:
                print(key + ":", countMainKeyWords[key])



    def getGenreFrequency(self):

        mainKeyWords = ["chinese", "japanese", "thai", "indian", "hyderabadi", "Mexican", "BBQ", "fries", "fry",
                        "chicken", "steak", "burger", "Pizza", "Nachos", "Pasta", "Soup", "Sandwich", "korean", "Italian",
                        "French", "rice", "Biriany"]

        with open('positiveReviews.csv', errors='ignore') as readFile:
            read_csv = csv.reader(readFile)
            data = list(csv.reader(readFile))

            number_of_rows = len(data)
            number_of_columns = len(data[0])
            searchSpace = []

            for rows in range(1, number_of_rows):
                searchSpace.append(data[rows][0])

            searchSpaceRows = len(searchSpace)

            countMainKeyWords = dict()

            for rows in range(0, searchSpaceRows):
                for key in mainKeyWords:
                    if str(searchSpace[rows]).lower().find(str(key).lower()) != -1:
                        if key in countMainKeyWords:
                            countMainKeyWords[str(key)] += 1
                        else:
                            countMainKeyWords[key] = 1

            for key in mainKeyWords:
                print(key + ":", countMainKeyWords[key])

    def getRelatedAdjectiveFrequency(self):

        mainKeyWords = ["Food", "Decoration", "Music", "Behavior", "Waiter", "Staff",
                        "Service", "Taste", "Environment", "Price", "Place"]

        adjectives = [["good", "delicious", "yummy", "health", "amazing", "testy", "awesome", "enjoy",
                        "great", "fresh", "spicy", "sweet",  "quality", "best"],
                      ["excellent", "well", "nice", "best", "unique"],
                      ["song", "good", "stage"],
                      ["hospitality", "friendly", "nice", "well", "frankly"],
                      ["friendly", "frankly", "well", "awesome"],
                      ["friendly", "frankly", "well", "awesome", "good"],
                      ["good", "amazing", "excellent", "best"],
                      ["good", "delicious", "yummy", "amazing"],
                      ["ambience", "excellent", "homely", "nice",
                        "quite", "comfortable", "welcoming", "frequent", "relaxed", "best"],
                      ["reasonable", "best"],
                      ["enjoy", "nice", "comfortable", "best"]]

        # print(len(mainKeyWords))
        # print(len(adjectives))

        with open('positiveReviews.csv', errors='ignore') as readFile:
            read_csv = csv.reader(readFile)
            data = list(csv.reader(readFile))

            number_of_rows = len(data)
            number_of_columns = len(data[0])
            searchSpace = []

            for rows in range(1, number_of_rows):
                searchSpace.append(data[rows][0])

            searchSpaceRows = len(searchSpace)

            countSubKey = dict()

            counter = 0

            for key in mainKeyWords:
                for rows in range(0, searchSpaceRows):
                    if str(searchSpace[rows]).lower().find(str(key).lower()) != -1 and counter < 11:
                        for subKey in adjectives[counter]:
                            print(subKey)
                            if subKey in countSubKey:
                                countSubKey[str(subKey)] += 1
                                counter = counter + 1
                            else:
                                countSubKey[str(subKey)] = 1
                                counter = counter + 1

                print("Subkeys for the word: " + str(key))
                for count in adjectives[counter]:
                    print(count + ":", countSubKey[count])
                countSubKey.clear()
                counter = 0

