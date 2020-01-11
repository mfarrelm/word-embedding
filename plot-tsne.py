#!/usr/bin/env python
# coding: utf-8

# In[2]:



import sys
import gensim
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import getopt
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)



# In[16]:

model = gensim.models.word2vec.Word2Vec.load('w2v_embedding_200M_128dim.model')
def tsne_plot(list_word, dpi = 400):

    #"Creates and TSNE model and plots it"
    labels = []
    tokens = []

    for word in (list_word):
            tokens.append(model[word])
            labels.append(word)

    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=3500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])

    plt.figure(figsize=(25, 25))
    for i in range(len(x)):
        plt.scatter(x[i],y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.savefig('tsne_plot.jpg', format='jpg', dpi=dpi)

def create_similar_word(a):
    list_word = []
    for word in a:
        word_similar = model.wv.most_similar(word, topn = int(500/len(a) - 1))
        for sim_word, _ in word_similar :
            list_word.append(sim_word)
        list_word.append(word)
    return list_word



# In[ ]:



list_word = sys.argv[1:]
list_word = create_similar_word(list_word)
print(list_word)
print('total kata : ', len(list_word))
tsne_plot(list_word)
