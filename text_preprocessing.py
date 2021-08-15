import re
from nltk.stem import PorterStemmer
import string
from nltk.corpus import stopwords
import pandas as pd
import nltk
tweets = pd.read_csv(r'C:\Users\admin\Desktop\Projects\scraped_data.csv')
X=tweets['Text']
nltk.download('stopwords')
stop_words=stopwords.words('english')
punct=string.punctuation
stemmer=PorterStemmer()
cleaned_data=[]
for i in range(len(X)):
    tweet=re.sub('[^a-zA-Z]', ' ', X.iloc[i])
    tweet=tweet.lower().split()
    tweet=[stemmer.stem(word) for word in tweet if (word not in stop_words) and (word not in punct)]
    tweet=' '.join(tweet)
    cleaned_data.append(tweet)
for i in range (len(cleaned_data)):
    print(cleaned_data[i])

# Creating a dataframe from the cleaned list above
print("Exporting it to cleaned_data.csv...")
cleaned_data2 = pd.DataFrame(cleaned_data)
cleaned_data2.to_csv(r'C:\Users\admin\Desktop\Projects\cleaned_data.csv')
print("Exported to cleaned_data.csv successfully!")
