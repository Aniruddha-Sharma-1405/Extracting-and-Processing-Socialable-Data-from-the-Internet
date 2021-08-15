from pickle import encode_long
import pandas as pd
import nltk
from pprint import pprint
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.text import Text
import re
from nltk.stem import PorterStemmer
import string
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import numpy as nump


def text_to_tokens(text_seqs):
    token_seqs = []
    for i in text_seqs:
      x = i.lower().split()
      token_seqs.append(x)
    return token_seqs

filtered_p=pd.read_csv(r'E:\VIT\Semester-4\CSE4022 (NLP)\Project\Codes\Dataset\pos_cleaned_data.csv')
filtered_n=pd.read_csv(r'E:\VIT\Semester-4\CSE4022 (NLP)\Project\Codes\Dataset\neg_cleaned_data.csv')
p1=filtered_p['0']
n1=filtered_n['0']

pt=text_to_tokens(p1)
nt=text_to_tokens(n1)
N=[]
P=[]
sia=SentimentIntensityAnalyzer()
for t in nt:
    for s in t:
        A=sia.polarity_scores(s)
        print(A)
        if(A['neg']==1.0):
            N.append(s)
for t in pt:
    for s in t:
        B=sia.polarity_scores(s)
        print(B)
        if(B['pos']==1.0):
            P.append(s)     

ncount=0
pcount=0
All_Neg = []
for i in N:
    if i not in All_Neg:
        All_Neg.append(i)
    ncount=ncount+1
All_Pos = []
for i in P:
    if i not in All_Pos:
        All_Pos.append(i)
    pcount=pcount+1

print(All_Neg)
print(All_Pos)
AN=pd.DataFrame(All_Neg)
AP=pd.DataFrame(All_Pos)

AN.to_csv(r'E:\VIT\Semester-4\CSE4022 (NLP)\Project\Codes\Dataset\trained_neg.csv')
AP.to_csv(r'E:\VIT\Semester-4\CSE4022 (NLP)\Project\Codes\Dataset\trained_pos.csv')

pos_date1 = pd.read_csv(r'E:\VIT\Semester-4\CSE4022 (NLP)\Project\Codes\Dataset\positive_data.csv')
neg_date1 = pd.read_csv(r'E:\VIT\Semester-4\CSE4022 (NLP)\Project\Codes\Dataset\negative_data.csv')
pos_date = pos_date1['Datetime']
neg_date = neg_date1['Datetime']
pc_2014=0
pc_2015=0
pc_2016=0
pc_2017=0
pc_2018=0
pc_2019=0
pc_2020=0
pc_2021=0

nc_2014=0
nc_2015=0
nc_2016=0
nc_2017=0
nc_2018=0
nc_2019=0
nc_2020=0
nc_2021=0
for i in pos_date:
    if i.startswith("2014"): 
        pc_2014 = pc_2014+1
    elif i.startswith("2015"):
        pc_2015 = pc_2015+1
    elif i.startswith("2016"):
        pc_2016 = pc_2016+1
    elif i.startswith("2017"):
        pc_2017 = pc_2017+1
    elif i.startswith("2018"):
        pc_2018 = pc_2018+1
    elif i.startswith("2019"):
        pc_2019 = pc_2019+1
    elif i.startswith("2020"):
        pc_2020 = pc_2020+1
    elif i.startswith("2021"):
        pc_2021 = pc_2021+1

for i in neg_date:
    if i.startswith("2014"):
        nc_2014 = nc_2014+1
    elif i.startswith("2015"):
        nc_2015 = nc_2015+1
    elif i.startswith("2016"):
        nc_2016 = nc_2016+1
    elif i.startswith("2017"):
        nc_2017 = nc_2017+1
    elif i.startswith("2018"):
        nc_2018 = nc_2018+1
    elif i.startswith("2019"):
        nc_2019 = nc_2019+1
    elif i.startswith("2020"):
        nc_2020 = nc_2020+1
    elif i.startswith("2021"):
        nc_2021 = nc_2021+1
p_allcounts = [pc_2014, pc_2015, pc_2016, pc_2017, pc_2018, pc_2019, pc_2020, pc_2021]
n_allcounts =[nc_2014, nc_2015, nc_2016, nc_2017, nc_2018, nc_2019, nc_2020, nc_2021]
years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
plt.subplot(2,2,3)
plt.title("Positive opinions")
plt.plot(years, p_allcounts)

plt.subplot(2,2,4)
plt.title("Negative opinions")
plt.plot(years, n_allcounts)


y=nump.array([ncount,pcount])
ml=["Negative","Positive"]
plt.subplot(2,2,1)
plt.pie(y, labels = ml,autopct='%1.2f%%')
plt.show()
