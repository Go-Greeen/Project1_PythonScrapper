import os
import csv
import requests
from bs4 import BeautifulSoup

hacker_url = "https://news.ycombinator.com"


def extract_infos():
  result = requests.get(hacker_url)
  soup = BeautifulSoup(result.text, "html.parser")
  all_news = soup.find_all("tr", {"class":"athing"})
  titles = []
  values = []
  for i in all_news:
    news = i.find_all("td", {"class":"title"})
    for x in news:
      title_link = x.find("a")
      try:
        values.append(title_link)
        each_title = title_link.string
        titles.append(each_title)
      except:
        ValueError
  values = values[1::2]
  links = []
  for q in values:
    a = q.get("href")
    links.append(a)
  title_and_link =[]
  for w,z in zip(titles, links):
    my_dict = {"Title":w, "Links":z}
    title_and_link.append(my_dict)
  
  subtext = soup.find_all("td", {"class":"subtext"})
  POINT = []
  USER_NAME = []
  COMMENTS_NUM = []
  COMMENTS_LINK = []
  SHORT_LINK = []
  for k in subtext:
#    try:
#      if sub_info != None:   
    point = k.find("span", {"class":"score"})
    try:
      if point != None:
        point = point.string
        POINT.append(point)
      else:
        point = None
        POINT.append(point)
    except:
      TypeError
    user_name = k.find("a", {"class":"hnuser"})
    try:
      if user_name != None:
        user_name = user_name.string
        USER_NAME.append(user_name)
      else:
        user_name = None
        USER_NAME.append(user_name)
    except:
      TypeError
    finding_comments = k.find_all("a")
    comments_num = finding_comments[-1]
    try:
      if comments_num != None:
        short_link = comments_num.get("href")
        SHORT_LINK.append(short_link)
        comments_link = f"https://news.ycombinator.com/{short_link}"
        COMMENTS_LINK.append(comments_link)
        comments_num = comments_num.string
        COMMENTS_NUM.append(comments_num)
    except:
      TypeError
  
  all_info = []
  for u in range(30):
    add_link = links[u]
    add_title = titles[u]
    add_point = POINT[u]
    add_user_name = USER_NAME[u]
    add_comments_num = COMMENTS_NUM[u]
    add_comments_link = COMMENTS_LINK[u]
    add_short_link = SHORT_LINK[u]
    add_dict = {"LINK":add_link, "TITLE":add_title, "POINT":add_point, "USER_NAME":add_user_name, "COMMENTS_NUM":add_comments_num, "COMMENTS_LINK":add_comments_link, "SHORT_LINK":add_short_link}
    all_info.append(add_dict)

    
  return all_info



def extract_comments(COMMENTS_LINK):
  USERS_COMMENTS =[]
  for i in COMMENTS_LINK:
    site_url = i.find_all("tr",{"class":"athing comtr "})
    i = []
    for z in site_url:
      user = z.find("a", {"class":"hnuser"})
      comment = z.find("span", {"class":"commtext c00"})
      user_comment = {"user":user, "comment":comment}
      i.append(user_comment)
    USERS_COMMENTS.append(i)
  print(USERS_COMMENTS)


  
  

  