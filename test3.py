# from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import numpy as np 
import arabic_reshaper
from bidi.algorithm import get_display
fin = []
#soup = BeautifulSoup(source,'lxml')
for a in range(1,2700):
    url ='https://engineering.uodiyala.edu.iq/news?ID='+ str(a)
    source=requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    title = soup.find('div',class_='articleShowCtrl')
    if title :
         fin1 = title.find('h3').text
         tex = arabic_reshaper.reshape(fin1)
         tex2=get_display(tex)
         fin.append(tex2)
    else:    
    # 
       fin.append("n/a")
    

print (fin)
df = pd.DataFrame(fin)
df.to_csv("data.csv",encoding="utf-8")

