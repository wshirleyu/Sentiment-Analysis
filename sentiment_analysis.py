#####
# Sentiment Analysis program
# By Shirley Wu
# Student number: 251082034

# Import punctuation from string module
from string import punctuation

# Define keytweetCount function to calculate the # of keyword tweets in each region
def keytweetCount(regionScores):
    keytweets = 0
    for i in regionScores:
        if i > 0:
            keytweets += 1
    return keytweets

# Define average function to calculate the average happiness score in each region
def average(scores, keyCount):
    if keyCount > 0:
        average = sum(scores) / keyCount
    else:
        average = 0
    return average

# Define findRegion function to determine where each region lies in the boundaries
def findRegion(long, lat):
    # Define constant values that relate to longitude and latitude, including max/min longitude values
    MAX_LONG = 49.189787
    MIN_LONG = 24.660845
    P1_LAT = -67.444574
    P3_LAT = -87.518395
    P5_LAT = -101.998892
    P7_LAT = -115.236428
    P9_LAT = -125.242264
    # Check longitude and latitude boundaries and return corresponding regions
    if MIN_LONG <= long <= MAX_LONG:
        if P1_LAT >= lat >= P3_LAT:
            return "eastern"
        elif P3_LAT >= lat >= P5_LAT:
            return "central"
        elif P5_LAT >= lat >= P7_LAT:
            return "mountain"
        elif P7_LAT >= lat >= P9_LAT:
            return "pacific"

# Define compute_tweets function with tweet file and keyword file as parameters
def compute_tweets(tweets, keywords):
    # Use try/except statement to handle potential IOErrors when opening tweet and keyword files
    try:
        # Use open function to open file for the try-block to access
        tweetFile = open(tweets, encoding='utf‐8', errors='ignore')
        # Ensures the tweet file is closed after opening
        tweetFile.close()
    except IOError:
        # If the files entered are wrong or do not exist, an empty list will be returned
        print("File not found.")
        return []
    try:
        keywordFile = open(keywords, encoding='utf‐8', errors='ignore')
        keywordFile.close()

    except IOError:
        print("File not found.")
        return []

    # Define dictionary to store keywords as keys along with their values
    keywordDict = {}

    # Define and initialize variables that count total number of tweets in each region
    easternCount = 0
    centralCount = 0
    mountainCount = 0
    pacificCount = 0

    # Create empty lists to store tweet scores in each region
    easternScores = []
    centralScores = []
    mountainScores = []
    pacificScores = []

    # Open keyword file in the compute_tweets function while avoiding encoding errors
    k = open(keywords, "r", encoding='utf-8', errors='ignore')
    # Call the "readline.()" method with "k" that was returned after opening the keyword file
    line = k.readline()

    # Loop through each line of the keyword file that contains text
    while line != "" and line != "\n":
        # Use ".strip()" method to remove spaces and ".split()" method to split each line at the commas
        words = line.strip().split(',')
        line = k.readline()
        # Use try/except to handle ValueErrors when opening files with wrong keyword file format
        try:
            # Using the keywordDict dictionary, assign each key at index 0 to its value at index 1
            keywordDict[words[0]] = int(words[1].strip())
        except ValueError:
            print("Keyword file is in wrong format.")
            break

    t = open(tweets, "r", encoding='utf‐8', errors='ignore')

    for tweet in t:
        # Define variables to store totals for keywords, sum of sentiment scores, and happiness scores with 0
        keywordCount = 0
        sentimentSum = 0
        happinessScore = 0
        # Use "if" statement to analyze tweets until the newline character "\n"
        if tweet != "\n":
            wordList = tweet.strip("[],").split()
            for word in wordList:
                word = word.strip(punctuation)
                word = word.lower()
                if word in keywordDict:
                    # If a word matches with a keyword in the dictionary, add 1 to the keyword count
                    keywordCount += 1
                    # Add the value of the keyword to the tweet's sum of sentiment scores of the tweet
                    sentimentSum += keywordDict[word]

            # Check if keywordCount is greater than 0 before division to avoid ZeroDivision Error
            if keywordCount > 0:
                happinessScore = sentimentSum / keywordCount

            # Ensure that there are existing words to loop through in wordLit
            if len(wordList) > 0:
                # Use try/except to handle ValueErrors when opening files with wrong tweet file format
                try:
                    # Assign values to the longitude and latitude variables by indices
                    long = float(wordList[0].strip(","))
                    lat = float(wordList[1].strip("[],"))
                except ValueError:
                    print("Tweet file is in wrong format.")
                    break

            # Use findRegion function to determine specific region
                region = findRegion(long, lat)
                # Add 1 to count of tweets in the region
                if region == "eastern":
                    # Use ".append()" method to add the happiness score to region's score list
                    easternCount += 1
                    easternScores.append(happinessScore)
                elif region == "central":
                    centralCount += 1
                    centralScores.append(happinessScore)
                elif region == "mountain":
                    mountainCount += 1
                    mountainScores.append(happinessScore)
                elif region == "pacific":
                    pacificCount += 1
                    pacificScores.append(happinessScore)

    # Use average function to calculate average happiness value in each region
    easternAvg = average(easternScores, keytweetCount(easternScores))
    centralAvg = average(centralScores, keytweetCount(centralScores))
    mountainAvg= average(mountainScores, keytweetCount(mountainScores))
    pacificAvg = average(pacificScores, keytweetCount(pacificScores))

    tweetFile.close()
    keywordFile.close()
    # Return list of tuples containing average happiness, # of keyword tweets, and # of tweets for each region
    return [(easternAvg, keytweetCount(easternScores), easternCount), (centralAvg, keytweetCount(centralScores), centralCount), (mountainAvg, keytweetCount(mountainScores), mountainCount), (pacificAvg, keytweetCount(pacificScores), pacificCount)]
