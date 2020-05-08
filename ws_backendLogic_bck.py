#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:16:39 2020

@author: meghanajagadish
"""
from datetime import datetime
import requests,sys
from math import log2,sqrt
import os,re,string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import warnings
import pickle as pickle

warnings.filterwarnings('ignore')
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def web_scraper():
    index=0
    count=0 
    for ele in (submit_url):
        
        f= open(folder+"/"+str(submit_url.index(ele)),"w+")
        File_name = str(submit_url.index(ele))
        f.truncate(0)
        try:
            r= requests.get(("https://"+ele),verify=False)
            print(submit_url.index(ele))
            raw=r.text
            print(ele)
            f.write(r.text)
            url_file[File_name]=ele  
            index+=1 
            f.close()
             
            soup = BeautifulSoup(str(raw), "html.parser")
            """
            find all links and 
            append to list to traveresed if it it not travered before
            """
            for a in soup.find_all('a', href=True):
                if (a['href']).startswith("https://")or(a['href']).startswith("http://"):
                    link = a['href'].split('://')[1]
                    if (link)[-1:] == "/":
                        (link)=(link)[:-1]
                        if link not in submit_url and ((len(submit_url))<30):
                            if "uic.edu" in link:
                                submit_url.append(link)
           
          
        except  Exception:
            print("Unexpected error:", sys.exc_info())
            count+=1
            pass
       
    print("Number of Exception",count)
    print("number of urls",len(submit_url))
    return url_file

def create_dictionary(file):
    text=""
    word_list=[]
    stop_words = set(stopwords.words("english"))
    soup = BeautifulSoup((file), "html.parser")
    #print("---------")
    list_of_tags=["h1","div","title","span","h2","h3","h4","h5","h6","p"]
    for tag in list_of_tags:
        for ele in soup.find_all(tag):
            text= text + ele.get_text()
    text.translate(str.maketrans('', '', string.punctuation))
    text=re.sub('[0-9]+', '', text)
    tokens = word_tokenize(text)
    words = [word for word in tokens if word.isalpha()]
    words = [word.lower() for word in words]
    ps = PorterStemmer()
    for r in words:
        if r not in stop_words:
            r = ps.stem(r)
            if(len(r)>2): 
                word_list.append(r)
    return word_list

def calc_tf(dict_): 
    for docId,texts in dict_.items(): 
        freq={}
        mx=1
        result=[]
        for words in texts:
            result.append(texts.count(words))
            freq[words] = texts.count(words)
        mx=max(result)
        freq = {k: v / mx for k, v in freq.items()}
        doc_tf.update({docId:freq})
       
def calc_idf(unique_word):
    f=0.0
    temp1={}
    doc_present={}
    dc=0
    for doc_id,tf in doc_tf.items():
        for word in tf.keys():
            if word in unique_word: 
                dc=dc+1
                doc_present.update({ doc_id: tf[word]})
    f=log2((len(doc_tf))/dc)
    idf_[unique_word]=f
    temp1.update({f:doc_present})
    return temp1
    
def calc_length(): 
    for doc_id,tf in doc_tf.items(): 
        tweight=0
        temp_={}
        for words in tf.keys():
            w=0
            w=tf[words]*(idf_[words])
            tweight+= (w ** 2)
            temp_[words]=w
        file_tfidf[doc_id]=temp_          
        length[doc_id]=sqrt(tweight)
    #print(file_tfidf)
    
def pre_process_query(text):
    word_list=[]
    stop_words = set(stopwords.words("english"))
    text.translate(str.maketrans('', '', string.punctuation))
    text=re.sub('[0-9]+', '', text)
    tokens = word_tokenize(text)
    words = [word for word in tokens if word.isalpha()]
    words = [word.lower() for word in words]
    ps = PorterStemmer()
    for r in words:
        if r not in stop_words:
            r = ps.stem(r)
            if(len(r)>2):
                word_list.append(r)
    return word_list

def calc_tf_query(value): 
    query_tf={}
    q_id=0
    qfreq={}
    result=[]
    mx=1
    for words in value:
        result.append(value.count(words))
        qfreq[words] = value.count(words)
    mx=max(result)
    qfreq = {k: v / mx for k, v in qfreq.items()}
    query_tf.update({q_id:qfreq})
    return query_tf

def calc_length_query(query_tf,idf_): 
    tf_idf_query={}
    q_length=[]
    for qid,qtf in query_tf.items(): 
        qtweight=0
        temp_={}
        for word in qtf.keys():
            qw=0
            if word in idf_.keys():
                qw=qtf[word]*(idf_[word])
            else:
                qw=qtf[word]
            qtweight+= (qw ** 2)
            temp_[word]=qw
        tf_idf_query.update({qid:temp_}) 
        q_length.append(sqrt(qtweight))
    return q_length,tf_idf_query
        

    
if __name__ == "__main__": 
    
    dict_={}
    unique_=[]
    doc_tf={}
    weight={}
    inverted_index={}
    idf_= {}
    length={}
    total_list = []
    query_dict={}
    idf_query={}
    query_tf={}
    total_vocab_query=[]
    q_length={}
    tf_idf_query={}
    file_tfidf={}
    ranking={}
    #URL to start the web scraping.
    url = 'cs.uic.edu' 
    submit_url=[]
    submit_url.append(url)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    folder ="./srcaped_docs"
    url_file={}    
    url_file= web_scraper()     
    print (url_file)
    print ("done scraping") 
    ranklist=[]
    
    path_lists = os.listdir(os.path.abspath(folder))
    for i in path_lists:
        if i.isdigit():
            temp=[]
            f=open(folder+"/"+i,"rb+")
            readfile=f.read()
            j=int(i)
            temp = create_dictionary(readfile)
            total_list= total_list+temp
            dict_.update({j:temp})  
        
    my_set = set(total_list)
    unique_ = list(my_set)
    calc_tf(dict_)
    
    for word in unique_:
        temp = calc_idf(word)
        inverted_index.update({word:temp}) 
    
    #print(inverted_index)
    #inverted_index = word:{num_of_doc_perent:{docId:num_of_times_presemt doc_ID })
    calc_length() 
    
    pickle_out = open("Inverteddict.pickle","wb")
    pickle.dump(inverted_index, pickle_out)
    pickle_out.close()
    
    pickle_out = open("Length.pickle","wb")
    pickle.dump(length, pickle_out)
    pickle_out.close()
    
    pickle_out = open("url_file.pickle","wb")
    pickle.dump(url_file, pickle_out)
    pickle_out.close()
    
    pickle_out = open("idf_.pickle","wb")
    pickle.dump(idf_, pickle_out)
    pickle_out.close()
    
   
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
