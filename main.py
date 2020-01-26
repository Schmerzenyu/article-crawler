import requests
from bs4 import BeautifulSoup

link="https://pubs.acs.org/toc/jacsat/142/3"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r=requests.get(link, headers=headers)

soup=BeautifulSoup(r.text, "lxml")
title_list=soup.find_all("h5", class_="issue-item_title")
for i in range(len(title_list)):
   title=title_list[i].a.text.strip()
   print(title)