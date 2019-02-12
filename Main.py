# -*- coding: utf-8 -*-

import FileLoad
import PropertyFunctions
from sklearn.feature_extraction.text import TfidfVectorizer
import MachineAlgorithms

class Classifier(object):
    
    
    def __init__(self):
        
        
        f = FileLoad.fileLoad()
        daf = f.load2()                             #daf = DataFrame
        
        sp = PropertyFunctions.propertyFunctions()
        
        #for 3 different method values
        daf1 = daf                           
        daf2 = daf
        daf3 = daf
        
        
        #first function (word stemmer operations (tf-idf))
        
        print("\n")
        print("\n")      
        print("WORD STEMMER PROCESS (TF-IDF)")
        print("\n")
        print("\n")

        # for term frequency
        #bow_transformer = CountVectorizer(analyzer=sp.split_into_stem).fit(daf1['message'])
        #messages_bow = bow_transformer.transform(daf1['message'])


        #print (len(bow_transformer.vocabulary_)) #sum words
        #print (messages_bow)       #messages_bow value on bag of word 
        #print (messages_bow.shape)

        #bag of words counts property
        #print ('sparse matrix shape:', messages_bow.shape)
        #print ('number of non-zeros:', messages_bow.nnz)
        #print ('sparsity: %.2f%%' % (100.0 * messages_bow.nnz / (messages_bow.shape[0] * messages_bow.shape[1])))
        #print(messages_bow.toarray())

        #print("daf1: ",daf1.message.head(10).apply(sp.split_into_stem))
        tfidf_vectorizer = TfidfVectorizer(analyzer=sp.split_into_stem).fit(daf1['message'])
        tfidf_transform = tfidf_vectorizer.transform(daf1['message'])  #tf-idf value
        
        #print (tfidf2.toarray())
        #print (tfidf_transformer.idf_[bow_transformer.vocabulary_['yeni']]) #words tf-idf value"
        
        
        MachineAlgorithms.machineAlgorithms(tfidf_transform.toarray(),daf1["label"])

        
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        
        
        print("WORD PROCESS (TF-IDF)")
        print("\n")
        print("\n")

        tfidf_vectorizer2 = TfidfVectorizer(analyzer=sp.split_into2_stem).fit(daf2['message'])
        tfidf_transform2 = tfidf_vectorizer2.transform(daf1['message'])  #tf-idf value
        
        MachineAlgorithms.machineAlgorithms(tfidf_transform2.toarray(),daf2["label"])


        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        
        print("WORD STEMMER PROCESS (BIGRAM TF-IDF)")
        print("\n")
        print("\n")

        daf3_result= daf3.message.apply(sp.split_into3_stem)
        tfidf_vectorizer3 = TfidfVectorizer(ngram_range=(1,2))
        tfidf_transform3 = tfidf_vectorizer3.fit_transform(daf3_result)

        #value = tfidf_vectorizer3.get_feature_names()   # tfidf words
        
        MachineAlgorithms.machineAlgorithms(tfidf_transform3.toarray(),daf3["label"])
        
        


Classifier()
