# -*- coding: utf-8 -*-
"""MCQG.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yEtvmZJNUHxWrCNwFc74HeAquzFerN7y
"""

from pywsd.similarity import max_similarity
from pywsd.lesk import adapted_lesk
from pywsd.lesk import simple_lesk
from pywsd.lesk import cosine_lesk
from flashtext import KeywordProcessor
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize
import requests
import tkinter
import json
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import nltk
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('popular')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('all')

#Step 1- Import the text file/article that has to be used for MCQ generation

# path=sys.argv[1]





def splitTextToSents(art):
    s=[sent_tokenize(art)]
    s=[y for x in s for y in x]
    s=[sent.strip() for sent in s if len(sent)>15] #Removes all the sentences that have length less than 15 so that we can ensure that our questions have enough length for context
    return s
#print(sents)




def mapSents(impWords,sents):
    processor=KeywordProcessor() #Using keyword processor as our processor for this task
    keySents={}
    for word in impWords:
        keySents[word]=[]
        processor.add_keyword(word) #Adds key word to the processor
    for sent in sents:
        found=processor.extract_keywords(sent) #Extract the keywords in the sentence
        for each in found:
            keySents[each].append(sent) #For each keyword found, map the sentence to the keyword
    for key in keySents.keys():
        temp=keySents[key]
        temp=sorted(temp,key=len,reverse=True) #Sort the sentences according to their decreasing length in order to ensure the quality of question for the MCQ 
        keySents[key]=temp
    return keySents
#print(mappedSents)







def getWordSense(sent,word):
    word=word.lower() 
    if len(word.split())>0: #Splits the word with underscores(_) instead of spaces if there are multiple words
        word=word.replace(" ","_")
    synsets=wn.synsets(word,'n') #Sysnets from Google are invoked
    if synsets:
        wup=max_similarity(sent,word,'wup',pos='n')
        adapted_lesk_output = adapted_lesk(sent, word, pos='n')
        lowest_index=min(synsets.index(wup),synsets.index(adapted_lesk_output))
        return synsets[lowest_index]
    else:
        return None
#print("fin")


def getDistractors(syn,word):
    dists=[]
    word=word.lower()
    actword=word
    if len(word.split())>0: #Splits the word with underscores(_) instead of spaces if there are multiple words
        word.replace(" ","_")
    hypernym = syn.hypernyms() #Gets the hypernyms of the word
    if len(hypernym)==0: #If there are no hypernyms for the current word, we simple return the empty list of distractors
        return dists
    for each in hypernym[0].hyponyms(): #Other wise we find the relevant hyponyms for the hypernyms
        name=each.lemmas()[0].name()
        if(name==actword):
            continue
        name=name.replace("_"," ")
        name=" ".join(w.capitalize() for w in name.split())
        if name is not None and name not in dists: #If the word is not already present in the list and is different from he actial word
            dists.append(name)
    return dists
#print("fin")



def getDistractors2(word):
    word=word.lower()
    actword=word
    if len(word.split())>0: #Splits the word with underscores(_) instead of spaces if there are multiple words
        word=word.replace(" ","_")
    dists=[]
    url= "http://api.conceptnet.io/query?node=/c/en/%s/n&rel=/r/PartOf&start=/c/en/%s&limit=5"%(word,word) #To get ditractors from ConceptNet's API
    obj=requests.get(url).json()
    for edge in obj['edges']:
        link=edge['end']['term']
        url2="http://api.conceptnet.io/query?node=%s&rel=/r/PartOf&end=%s&limit=10"%(link,link)
        obj2=requests.get(url2).json()
        for edge in obj2['edges']:
            word2=edge['start']['label']
            if word2 not in dists and actword.lower() not in word2.lower(): #If the word is not already present in the list and is different from he actial word
                dists.append(word2)
    return dists

def main(path):
    file=open(path,"r") #"r" deontes read version open
    text=file.read()


    # tokenize text into individual words and remove stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = nltk.word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stop_words]

    # assign parts of speech to each word
    pos_tags = nltk.pos_tag(tokens)

    # identify named entities
    named_entities = nltk.ne_chunk(pos_tags)

    # extract named entities from tree structure
    named_entities = [' '.join(leaf[0] for leaf in subtree.leaves())
                    for subtree in named_entities
                    if hasattr(subtree, 'label') and subtree.label() == 'NE']

    # combine named entities with other important words
    important_words = named_entities + [word for word, pos in pos_tags if pos.startswith(('N', 'V', 'J'))]

    sents=splitTextToSents(text) #Achieve a well splitted set of sentences from the text article
    mappedSents=mapSents(important_words,sents) #Achieve the sentences that contain the keywords and map those sentences to the keywords using this function


    mappedDists={}
    for each in mappedSents:
        try:
            wordsense=getWordSense(mappedSents[each][0],each) #gets the sense of the word
            if wordsense: #if the wordsense is not null/none
                dists=getDistractors(wordsense,each) #Gets the WordNet distractors
                if len(dists)==0: #If there are no WordNet distractors available for the current word
                    dists=getDistractors2(each) #The gets the distractors from the ConceptNet API
                if len(dists)!=0: #If there are indeed distractors from WordNet available, then maps them
                    mappedDists[each]=dists
            else: #If there is no wordsense, the directly searches/uses the ConceptNet
                dists=getDistractors2(each)
                if len(dists)>0: #If it gets the Distractors then maps them
                    mappedDists[each]=dists
        except:
            pass
    #print(mappedDists)





    f=open("mcq.txt","a")
    g=open("mcq_ans.txt","a")

    print("**************************************        Multiple Choice Questions        *******************************")
    print()
    import re
    import random
    iterator = 1 
    for each in mappedDists:
        sent=mappedSents[each][0]
        p=re.compile(each,re.IGNORECASE) 
        g.write("A"+str(iterator)+" "+each+"\n")
        op=p.sub("________",sent) 
        print("Question %s-> "%(iterator),op) 
        f.write("\nQ"+str(iterator)+" "+op)
        options=[each.capitalize()]+mappedDists[each] 
        options=options[:4] 
        opts=['a','b','c','d']
        random.shuffle(options) 
        for i,ch in enumerate(options):
            print("\t",opts[i],") ", ch) 
            f.write("\n\t"+opts[i]+" ) "+ ch)
        print()
        iterator+=1 
    f.close()
    g.close()