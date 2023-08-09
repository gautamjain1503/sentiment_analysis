import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data = pd.read_excel('input.xlsx')
data["article"]=np.nan

for i in range(len(data)):
    try:
        print(i)
        temp_url=data.URL[i]
        r=requests.get(temp_url)
        soup=BeautifulSoup(r.text,'html.parser')
        temp_article_title=soup.find("h1")
        temp_article_content=(soup.find(class_="td-post-content tagdiv-type")).find_all(["p","h3"])
        temp=(temp_article_title.get_text())
        for j in temp_article_content:
            temp=temp+" "+(j.get_text())
        data["article"][i]=(temp)
    except:
        try:
            temp_url=data.URL[i]
            r=requests.get(temp_url)
            soup=BeautifulSoup(r.text,'html.parser')
            temp_article_title=soup.find(class_="td_block_wrap tdb_title tdi_122 tdb-single-title td-pb-border-top td_block_template_1")
            temp_article_content=(soup.find(class_="td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type")).find_all(["p","h3"])
            temp=(temp_article_title.get_text())
            for j in temp_article_content:
                temp=temp+" "+(j.get_text())
            data["article"][i]=temp
        except:
            continue


data.to_excel("web_scraped.xlsx",index=False)