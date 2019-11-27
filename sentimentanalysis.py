def compute_tweets(tweets, keywords):
    try:
        tweetFile = open(tweets, encoding='utf‐8', errors='ignore')
    except IOError:
        print("File not found.")
        return []
    try:
        keywordFile = open(keywords, encoding='utf‐8', errors='ignore')
    except IOError:
        print("File not found.")
        return []

    keywordDict = {}

    easternRegion = 0
    centralRegion = 0
    mountainRegion = 0
    pacificRegion = 0

    easternKeywords = 0
    centralKeywords = 0
    mountainKeywords = 0
    pacificKeywords = 0

    easternAverage = 0
    centralAverage = 0
    mountainAverage = 0
    pacificAverage = 0

    easternScores = []
    centralScores = []
    mountainScores = []
    pacificScores = []

    #k = open(keywordFile, encoding='utf‐8', errors='ignore')
    k = open(keywords, encoding='utf-8', errors='ignore')
    line = k.readline()

    while line != "":
        words = line.split(',')
        line = k.readline()
        keywordDict[words[0]] = int(words[1].strip())
    print(keywordDict)

    MAX_LONG = 49.189787
    MIN_LONG = 24.660845
    P1_LAT = -67.444574
    P3_LAT = -87.518395
    P5_LAT = -101.998892
    P7_LAT = -115.236428
    P9_LAT = -125.242264

    keywordCount = 0
    sentimentSum = 0
    happinessScore = 0

    t = open(tweets, encoding='utf‐8', errors='ignore')
    line = t.readline()

    for tweet in t:
        wordList = tweet.split()
        for word in wordList:
            word = word.strip(".,?![]")
            if word in keywordDict:
                keywordCount += 1
                sentimentSum += keywordDict[word]
        happinessScore = sentimentSum / keywordCount

        long = float(tweet[0])
        lat = float(tweet[1])

        while long <= MAX_LONG or long >= MIN_LONG:
            if lat <= P1_LAT and lat >= P3_LAT:
                easternRegion += 1
                if tweet in keywordDict:
                    easternKeywords += 1
                    easternScores.append(int(happinessScore))
            elif lat <= P3_LAT and lat >= P5_LAT:
                centralRegion += 1
                if tweet in keywordDict:
                    centralKeywords += 1
                    centralScores.append(int(happinessScore))
            elif lat <= P5_LAT and lat >= P7_LAT:
                mountainRegion += 1
                if tweet in keywordDict:
                    mountainKeywords += 1
                    mountainScores.append(int(happinessScore))
            elif lat <= P7_LAT and lat >= P9_LAT:
                pacificRegion += 1
                if tweet in keywordDict:
                    pacificKeywords += 1
                    pacificScores.append(int(happinessScore))

    easternAverage = sum(easternScores / easternKeywords)
    centralAverage = sum(centralScores/ centralKeywords)
    mountainAverage = sum(mountainScores / mountainKeywords)
    pacificAverage = sum(pacificScores / pacificKeywords)

    return(easternAverage, easternScores, easternKeywords)
    return(centralAverage, centralScores, centralKeywords)
    return(mountainAverage, mountainScores, mountainKeywords)
    return(pacificAverage, pacificScores, pacificKeywords)

