import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

def a_country(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def main():
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  get_info = soup.find("tbody").find_all("td")
  country_info =[]
  for i in get_info:
    country_info.append(i.string)
  country_name = country_info[::4]
  print("Hello! Please choose a country by number")
  for x, y in enumerate(country_name, start=1):
    print(x, y)
  each_country = list(a_country(country_info, 4))
  matter(each_country)


def matter(each_country):
  answer = input("#:")
  x = range(1, 268)
  try:
    answer = int(answer)
    if answer in x:
      print("You chose " + each_country[answer][0] + "\n" "The currency code is " + each_country[answer][2])
      return
    else:
      print("chose a number from the list")
      matter(each_country)
  except:
    answer = answer
    print("That wasn't a number.")
    matter(each_country)

main()
