import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets_list = []
keyword = input("Enter the hit word: ")
num = int(input("Enter the number of tweets to be analysed: "))
query = keyword+" "+"lang:en"
t1 = int(input("Do you want to specify a date range? (Enter 1 for yes and 0 for no): "))
if t1==1:
    since = input("Starting date (YYYY-MM-DD): ")
    to = input ("Ending date (YYYY-MM-DD): ")
    query = query+" since:"+since+"to:"+to
t2 = int(input("Do you want to specify a location? (Enter 1 for yes and 0 for no): "))
if t2==1:
    location = input("Enter location: ")
    query = query+"location:"+location
# print(query)

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i>num:
        break
    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.user.location])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Location'])
print(tweets_df2)
print("Exporting it to scraped_data.csv...")
tweets_df2.to_csv(r'C:\Users\admin\Desktop\Projects\scraped_data.csv')
print("Exported to scraped_data.csv successfully!")
