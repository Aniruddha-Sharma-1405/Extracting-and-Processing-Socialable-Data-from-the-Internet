import re
from nltk.stem import PorterStemmer
import string
from nltk.corpus import stopwords
import pandas as pd
import nltk

nltk.download('stopwords')
stop_words=stopwords.words('english')
punct=string.punctuation
stemmer=PorterStemmer()

def data_processing(X):
    cleaned_data=[]
    for i in range(len(X)):
        tweet=re.sub('[^a-zA-Z]', ' ', X.iloc[i])
        tweet=tweet.lower().split()
        tweet=[stemmer.stem(word) for word in tweet if (word not in stop_words) and (word not in punct)]
        tweet=' '.join(tweet)
        cleaned_data.append(tweet)
    for i in range (len(cleaned_data)):
        print(cleaned_data[i])
    return cleaned_data

p_file = pd.read_csv(r'E:\VIT\Semester-4\CSE4022 (NLP)\Project\Codes\Dataset\positive_data.csv')
pX = p_file['0']
p_cleaned = data_processing(pX)
p_cleaned2 = pd.DataFrame(p_cleaned)


n_file = pd.read_csv(r'E:\VIT\Semester-4\CSE4022 (NLP)\Project\Codes\Dataset\negative_data.csv')
nX = n_file['0']
n_cleaned = data_processing(nX)
n_cleaned2 = pd.DataFrame(n_cleaned)

p_cleaned2.to_csv(r'E:\VIT\Semester-4\CSE4022 (NLP)\Project\Codes\Dataset\pos_cleaned_data.csv')
print("Exported to pos_cleaned_data.csv successfully!")
n_cleaned2.to_csv(r'E:\VIT\Semester-4\CSE4022 (NLP)\Project\Codes\Dataset\neg_cleaned_data.csv')
print("Exported to neg_cleaned_data.csv successfully!")
