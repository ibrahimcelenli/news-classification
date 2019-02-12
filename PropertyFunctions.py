# -*- coding: utf-8 -*-

from nltk.corpus import stopwords
from textblob import TextBlob
from zemberek_parser.zemberek_python import main_libs as ml


class propertyFunctions(object):

    def __init__(self):

        global stop_words
        stop_words = set(stopwords.words("turkish"))  # stopwords words

        # jvm.dll path location
        self.zemberek_api = ml.zemberek_api(libjvmpath="/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server/libjvm.so",
                                       zemberekJarpath="./zemberek_python/zemberek-tum-2.0.jar").zemberek()

        # jvmDLLpath = r"C:\Program Files\Java\jdk1.7.0\jre\bin\server\jvm.dll"               # for windows

    # word root operations
    def split_into_stem(self, message):


        message = message.lower()
        words = TextBlob(message).words  # seperate message

        words = [w2 for w2 in words if not w2 in stop_words]  # stopwords remove
        return  ml.ZemberekTool(self.zemberek_api).metinde_gecen_kokleri_bul(words)


    def split_into2_stem(self,message):

        message = message.lower()
        words = TextBlob(message).words
        # print(words)

        return [w2 for w2 in words if not w2 in stop_words]  # stopwords remove

    # bigram use
    def split_into3_stem(self,message):



        message = message.lower()
        words = TextBlob(message)
        return (" ".join(ml.ZemberekTool(self.zemberek_api).metinde_gecen_kokleri_bul(words)))
