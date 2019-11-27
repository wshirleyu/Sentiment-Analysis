#
# Import compute_tweets function from "sentiment_analysis' module
from sentiment_analysis import compute_tweets

from string import punctuation


# Prompt user for the names of their tweet and keyword files
tweets = input("Enter tweet file: ")
keywords = input("Enter keyword file: ")

# Call the compute_tweets function with tweet and keyword files as parameters
result = compute_tweets(tweets, keywords)
print(result, "\n")

# Print results in readable format
if result != []:
    print("Eastern Region: ")
    print("   Happiness score: ", result[0][0])
    print("   Number of keyword tweets: ", result[0][1])
    print("   Total number of tweets: ", result[0][2], "\n")

    print("Central Region: ")
    print("   Happiness score: ", result[1][0])
    print("   Number of keyword tweets: ", result[1][1])
    print("   Total number of tweets: ", result[1][2], "\n")

    print("Mountain Region: ")
    print("   Happiness score: ", result[2][0])
    print("   Number of keyword tweets: ", result[2][1])
    print("   Total number of tweets: ", result[2][2], "\n")

    print("Pacific Region: ")
    print("   Happiness score: ", result[3][0])
    print("   Number of keyword tweets: ", result[3][1])
    print("   Total number of tweets: ", result[3][2], "\n")

# End of program



