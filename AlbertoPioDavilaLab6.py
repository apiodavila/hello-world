#Alberto Davila Lab 6
#partA
fileName = 'C:\\Users\\apiod\\Downloads\\tickerInfo.csv'
import pandas as pd
df = pd.read_csv(fileName)
maxClose = df['Close'].max()
print(maxClose)
closingPrices = list(df['Close'])

#partB
import matplotlib.pyplot as plt
x = range(len(closingPrices))
plt.plot(x, closingPrices)
plt.show()

#partC
comment = 'This is the best product I\'ve ever owned!'
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
sentimentScores = sid.polarity_scores(comment)
print(sentimentScores['compound'])

#partD
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'http://www.musicpriceguide.com'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
titleTags = soup.find_all(title = True)
for a in titleTags:
    print(a.get_text())
