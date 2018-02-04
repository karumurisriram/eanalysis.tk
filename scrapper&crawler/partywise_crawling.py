# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:45:21 2017

@author: jaiprakash
"""
import pandas as pd
import requests
import store_dataframe as sd
from bs4 import BeautifulSoup

links =["http://eciresults.nic.in/ConstituencywiseS06%s.htm?ac=%s",
        "http://eciresults.nic.in/ConstituencywiseS08%s.htm?ac=%s"]
kk = 6
no_pages  = [182,68]
lll =0 
for url in links:
    i = 1
    page = requests.get(url % (i,i))
    soup = BeautifulSoup(page.content,'html5lib')
    dd={}
    d = {}
    if(kk==8):
        for cons in soup.find('input', id='HdnHP').get('value').split(';'):
            o = cons.split(',')
            #print(kk,"hp")
            if(len(o)>1):
                d[o[0]]=o[1]
    else:
        for cons in soup.find('input', id='HdnGJ').get('value').split(';'):
            o = cons.split(',')
            #print(kk,"gj")
            if(len(o)>1):
                d[o[0]]=o[1]
    l = sorted([int(i) for i in d.keys()])
    for k in l:
        dd[k]=d[str(k)]
    #print(dd)
    list1 =[]
    consistutency = {}
    while i<=no_pages[lll]:

        page = requests.get(url % (i,i))

        soup = BeautifulSoup(page.content,'html5lib')
        
        soup = soup.find('div', id='div1')
        soup.select("tr")
        [x.select('td') for x in soup.select("tr")]
        
        d = [[y.text.replace(" ","") for y in x.select('td')] for x in soup.select("tr")[3:-2]]
        # df = pd.DataFrame(d, columns = ['party', 'won', 'lost', 'pend'])
        #d[1].append(dd[i])
        for dk in d:
            dk.append(dd[i])
        #print(d)
        list1.append(d)
        #if(len(d)>1):
        consistutency[dd[i]]=d
        #break

        
        i = i+1
    lll = lll +1
    Constitutency=[]
    Candidate=[]
    Votes=[]
    Party=[]
    for j in list1:
        print(j)
        for jj in j:
            Party.append(jj[1])
            Votes.append(jj[2])
            Candidate.append(jj[0])
            Constitutency.append(jj[3])
            #print('\n----\n',jj,'\n------\n')
    #print(Votes)
    #print(Party)
    df = pd.DataFrame({'Constitutency': Constitutency,
             'Candidate': Candidate,
             'Party': Party,
             'Votes':Votes,
     
        })
    print ('>>',df)
    df.to_csv("consistituency%s.csv"%kk, encoding='utf-8', index=True)
    sd.store("consistituency%s"%kk,df)
    kk=kk+2
    

