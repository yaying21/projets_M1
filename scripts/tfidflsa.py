import pandas as pd
import numpy as np
import sys
#     f.write("\n\n".join(pdf))
K = 2 # number of components
query = 'homme ou femme'
# Data filename
dataset_filename = "../fables/fables.csv"

# Loading dataset
data = pd.read_csv(dataset_filename,sep='\t')

# We are reducing the size of our dataset to decrease the running time of code
# data = data.loc[data['texte'] == 1078, :]
#
# # Delete missing observations for variables that we will be working with
# for x in ["Recommended IND", "Review Text"]:
#     datax = datax[datax[x].notnull()]
#
# # Keeping only those features that we will explore
# datax = datax[["Recommended IND", "Review Text"]]

# Resetting the index
data.index = pd.Series(list(range(data.shape[0])))

print('Shape : ', data.shape)
print(data.head())
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

wordnet_lemmatizer = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'[a-z]+')
stop_words = set(stopwords.words('french'))

def preprocess(document):
    document = document.lower() # Convert to lowercase
    words = tokenizer.tokenize(document) # Tokenize
    words = [w for w in words if not w in stop_words] # Removing stopwords
    # Lemmatizing
    for pos in [wordnet.NOUN, wordnet.VERB, wordnet.ADJ, wordnet.ADV]:
        words = [wordnet_lemmatizer.lemmatize(x, pos) for x in words]
    return " ".join(words)
data['Processed Review'] = data['texte'].apply(preprocess)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
TF_IDF_matrix = vectorizer.fit_transform(data['Processed Review'])
TF_IDF_matrix = TF_IDF_matrix.T

print('Vocabulary Size : ', len(vectorizer.get_feature_names()))
print('Shape of Matrix : ', TF_IDF_matrix.shape)
import numpy as np

# Applying SVD
U, s, VT = np.linalg.svd(TF_IDF_matrix.toarray()) # .T is used to take transpose and .toarray() is used to convert sparse matrix to normal matrix

TF_IDF_matrix_reduced = np.dot(U[:,:K], np.dot(np.diag(s[:K]), VT[:K, :]))

# Getting document and term representation
terms_rep = np.dot(U[:,:K], np.diag(s[:K])) # M X K matrix where M = Vocabulary Size and N = Number of documents
docs_rep = np.dot(np.diag(s[:K]), VT[:K, :]).T # N x K matrix

import matplotlib.pyplot as plt

# %matplotlib inline
#
plt.scatter(docs_rep[:,0], docs_rep[:,1], c=data['LABEL'])
plt.title("Document Representation")
plt.show()
plt.scatter(terms_rep[:,0], terms_rep[:,1])
plt.title("Term Representation")
plt.show()
# sys.exit()

def lsa_query_rep(query):
    query_rep = [vectorizer.vocabulary_[x] for x in preprocess(query).split()]
    query_rep = np.mean(terms_rep[query_rep],axis=0)
    return query_rep

from scipy.spatial.distance import cosine

query_rep = lsa_query_rep(query)

query_doc_cos_dist = [cosine(query_rep, doc_rep) for doc_rep in docs_rep]
query_doc_sort_index = np.argsort(np.array(query_doc_cos_dist))

print_count = 0
for rank, sort_index in enumerate(query_doc_sort_index):
    print ('Rank : ', rank, ' Consine : ', 1 - query_doc_cos_dist[sort_index],' Review : ', data['Processed Review'][sort_index])
    if print_count == 10 :
        break
    else:
        print_count += 1

