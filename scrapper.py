import os
import requests
from bs4 import BeautifulSoup

os.system("clear")


url = "https://www.iban.com/currency-codes"


countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code =items[2].text
  if name and code:
    if name != "No universal currency":
      country = {
        'name':name.capitalize(),
        'code': code
      }
      countries.append(country)


def ask():
  try:
    choice = int(input("\nWhere are you from? Choose a country by number.\n#: "))
    if choice > len(countries):
      print("Choose a number from the list.")
      ask()
    else:
      country = countries[choice]
      print(f"{country['name']}")
      ask2(country)
  except  ValueError:
    print("That wasn't a number.")
    ask()


def ask2(country):
  try:
    choice2 = int(input("\nChoose another country.\n#: "))
    if choice2 > len(countries):
      print("Choose a number from the list.")
      ask2(country)
    else:
      country2 = countries[choice2]
      print(f"{country2['name']} \n\nHow much {country['code']} do you want to convert to {country2['code']}?")
      ask3(country, country2)
  except ValueError:
    print("That wasn't a number.")
    ask2(country)

  
def ask3(country, country2):
  choice3 = input()
  URL = f"https://transferwise.com/gb/currency-converter/{country['code']}-to-{country2['code']}-rate?amount={choice3}"
  request2 = requests.get(URL)
  if request2.status_code == 200:      
    soup2 = BeautifulSoup(request2.text, "html.parser")
    text = soup2.find("div", {"class":"col-lg-6 text-xs-center text-lg-left"})
    span = text.find("span", {"class":"text-success"}).string
    print(f"{country['code']}{choice3} is {country2['code']}{float(span)*float(choice3)}")
  else:
    print("That's not a number.")
    ask3(country, country2)


print("Welcome to CurrencyConvert PRO 2000\n")
for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")

ask()