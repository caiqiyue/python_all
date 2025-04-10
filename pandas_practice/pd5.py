import pandas as pd


data = [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']]
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})

print(tweets[tweets['content'].map(lambda x:True if len(x) <= 15 else False)])

    