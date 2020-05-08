#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:40:47 2020

@author: meghanajagadish
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:00:47 2020

@author: meghanajagadish
"""

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pickle as pickle
import ws_backendLogic as ws
import tkinter as tk


def new_cosine(q_tfidf,query_id):
    cosine_rank={}
    for qword ,val in q_tfidf.items():
        for tkn,count in inverted_index.items():
            if qword in tkn:
                for list_doc in count.values():
                    for docid , value in list_doc.items():
                        if docid in cosine_rank.keys():
                            m=q_length[query_id]*length[docid]
                            cosine_rank[docid]+= (val*(value*idf_[qword]))/m
                        else:
                            m=q_length[query_id]*length[docid]
                            cosine_rank[docid]= (val*(value*idf_[qword]))/m  
                    
    sorted_rank = sorted(cosine_rank.items(), key=lambda kv:kv[1],reverse=True)
    srt_csn=[]
    srt_csn = [x for x,v in sorted_rank]
    return srt_csn 
      
      
def print_results(strt,end,val):
    for ele in ranklist[strt:end]:
        print(url_file[str(ele)])
    if(val==1):
        print("NO MORE RESULTS TO SHOW")

def output(query_):
    global query_tf
    global q_length
    global tf_idf_query
    

if __name__ == "__main__":
    
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    inverted_index={}
    length={}
    ranking={}
    idf_query={}
    tf_idf_query={}
    q_id=1
    
    ranklist=[]
    #URL to start the web scraping.
    #url_file
    pickle_in = open("idf_.pickle","rb")
    idf_ = pickle.load(pickle_in)
    #print(idf_)
    
    pickle_in = open("Inverteddict.pickle","rb")
    inverted_index = pickle.load(pickle_in)
    #print(inverted_index)
     
    pickle_in = open("length.pickle","rb")
    length = pickle.load(pickle_in)
    #print(length)
     
    pickle_in = open("url_file.pickle","rb")
    url_file = pickle.load(pickle_in)
    
    
    print(url_file)
    
    
    query_ = input("Enter the query: ")
    tokens_query=ws.pre_process_query(query_)
    my_set = set(tokens_query)
    unique_query = list(my_set)
   
    query_tf =ws.calc_tf_query(tokens_query) 
    for word in unique_query:
        idf_query[word]=1
            
    q_length,tf_idf_query= ws.calc_length_query(query_tf,idf_)
        
    for query_id ,q_tfidf in tf_idf_query.items():
        ranklist = new_cosine(q_tfidf,query_id)
    
    
    
    print("full ranks", ranklist)
    if(len(ranklist)< 10):
        print("There are only ", len(ranklist), "results for the entered query!!!")
        end = (len(ranklist))
        val=1
    print_results(start,end,val) 
               
    
    start=0
    end=10
    val=0
    while(end<=(len(ranklist)-1)):
        rl = input("Load more result Y ,N")
        if(rl.lower()=='n'):
            break
        elif(rl.lower()=='y'):
            if (end+10)==(len(ranklist)-1) or (end+10)>(len(ranklist)-1):
                start = start+10
                end = (len(ranklist))
                val=1
                print_results(start,end,val) 
                break
            else:
                start = start+10
                end=end+10
                print_results(start,end,val) 
        else:
            print("INVALID INPUT")
        
        
        