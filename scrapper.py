 
  
 
import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"



result = requests.get(alba_url)
soup = BeautifulSoup(result.text, "html.parser")
super_brand = soup.find("div", {"id":
"MainSuperBrand"}).find_all("span", {"class":"company"})
jobs = []
for i in super_brand:
  i = i.string
  try:
    if i != None:
      jobs.append(i)
  except:
    TypeError


brand = soup.find("div", {"id":"MainSuperBrand"}).find_all("a",{"class":"goodsBox-info","href":True})
site_urls = []
for i in brand:
  key = i['href']
  site_urls.append(key)

for w,y in zip(jobs,site_urls):
  new_result = requests.get(y)
  new_soup = BeautifulSoup(new_result.text, "html.parser")
  albas = new_soup.find("tbody")
  location = albas.find_all("td", {"class":"local first"})
  LOCATION = []
  for i in location:
    if i != None:
      i = i.text
      LOCATION.append(i)
    else:
      LOCATION.append(None)

  COMPANY = []
  company = albas.find_all("span",{"class":"company"})
  for i in company:
    if i != None:
      i = i.text
      COMPANY.append(i)
    else:
      COMPANY.append(None)

  HOUR = []
  hour = albas.find_all("span",{"class":"time"})
  for i in hour:
    if i != None:
      i = i.text
      HOUR.append(i)
    else:
      HOUR.append(None)

  PAY = []
  pay = albas.find_all("td",{"class":"pay"})
  for i in pay:
    if i != None:
      i = i.text
      PAY.append(i)
    else:
      PAY.append(None)


  UPLOADED = []
  uploaded = albas.find_all("td", {"class":"regDate last"})
  for i in uploaded:
    if i != None:
      i = i.text
      UPLOADED.append(i)
    else:
      UPLOADED.append(None)


  all_info = []
  number = len(HOUR)
  x = range(number)
  for i in x:
    a = LOCATION[i]
    b = COMPANY[i]
    c = HOUR[i]
    d = PAY[i]
    e = UPLOADED[i]
    info_dict = {"location":a, "company":b, "time":c, "pay":d, "date":e}
    all_info.append(info_dict)
  print(all_info)


  def save_to_file(w, all_info):
    file = open(f"{w}.csv", encoding='utf-8-sig', mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "comapny", "location", "link"])
    for i in all_info:
      writer.writerow(list(i.values()))
    

  save_to_file(w, all_info)



