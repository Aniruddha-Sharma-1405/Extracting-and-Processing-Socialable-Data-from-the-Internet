import pandas as pd
import nltk
import codecs
from nltk.tokenize import PunktSentenceTokenizer,sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer, PorterStemmer
import os

def simpleFilter(sentence):#This function is used to simplify the sentence by only lemmatization

    filtered_sent = []
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(w))
    return filtered_sent
def simlilarityCheck(word1, word2):#To check simlilarity between the words of the query and document.

    word1 = word1 + ".n.01"
    word2 = word2 + ".n.01"
    try:
        w1 = wordnet.synset(word1)
        w2 = wordnet.synset(word2)

        return w1.wup_similarity(w2)

    except:
        return 0
def synonymsCreator(word):#Used to get the synonyms of the words
    synonyms = []

    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            synonyms.append(i.name())

    return synonyms
def filteredSentence(sentence):#It process the sentences with both stemming and then giving the rootword or lemma

    filtered_sent = []
    lemmatizer = WordNetLemmatizer()  # lemmatizes the words
    ps = PorterStemmer()  # stemmer stems the root of the word.

    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)

    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(ps.stem(w)))
            for i in synonymsCreator(w):
                filtered_sent.append(i)
    
    return filtered_sent


base_path = "E:\\VIT\\Semester-4\\CSE4022 (NLP)\\Project\\Codes\\Dataset"
filename = "realThreats.txt"
path_to_file = os.path.join(base_path, filename)
threats = open(path_to_file , 'r', encoding='utf-8')
sent2=threats.read().lower()


file2="notThreats.txt"
pathfile=os.path.join(base_path,file2)
notThreats=open(pathfile,'r',encoding='utf-8')
sent1=notThreats.read().lower()

threatlist=[]
nonthreatlist=[]

tweets = pd.read_csv(r'E:\VIT\Semester-4\CSE4022 (NLP)\Project\Codes\Dataset\negative_data.csv')
X=tweets['0']
# X = ["Today is not possible to attack parliament building."]

for z in range (len(X)):
    sent3=X[z]

    filtered_sent1 = []
    filtered_sent2 = []
    filtered_sent3 = []

    sent31_similarity = 0
    sent32_similarity = 0

    filtered_sent1 = simpleFilter(sent1)
    filtered_sent2 = simpleFilter(sent2)
    filtered_sent3 = simpleFilter(sent3)

    for i in filtered_sent3:
        for j in filtered_sent1:
            sent31_similarity = sent31_similarity + simlilarityCheck(i, j)

        for j in filtered_sent2:
            sent32_similarity = sent32_similarity + simlilarityCheck(i, j)

    filtered_sent1 = []
    filtered_sent2 = []
    filtered_sent3 = []

    filtered_sent1 = filteredSentence(sent1)
    filtered_sent2 = filteredSentence(sent2)
    filtered_sent3 = filteredSentence(sent3)

    sent1_count = 0
    sent2_count = 0
    c=0
    k=0
    for i in list(set(filtered_sent3)):
 
        for j in filtered_sent1:
            if(i == j):
                sent1_count = sent1_count + 1


        for j in filtered_sent2:
            if(i == j):
                sent2_count = sent2_count + 1
        
    if((sent31_similarity + sent1_count) > (sent32_similarity + sent2_count)):
        # print(sent3 + " - NOT THREAT" , sent31_similarity, sent32_similarity, "\n\n")
        nonthreatlist.append(sent3)
    else:
        print(sent3 + " - THREAT" , sent31_similarity, sent32_similarity, "\n\n")
        threatlist.append(sent3)

threat2 = pd.DataFrame(threatlist)
threat2.to_csv(r'E:\VIT\Semester-4\CSE4022 (NLP)\Project\Codes\Dataset\threat_data.csv')
print("Exported to threat_data.csv successfully!")

nonthreat2 = pd.DataFrame(nonthreatlist)
nonthreat2.to_csv(r'E:\VIT\Semester-4\CSE4022 (NLP)\Project\Codes\Dataset\nonthreat_data.csv')
print("Exported to nonthreat_data.csv successfully!")
