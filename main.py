import requests
from bs4 import BeautifulSoup

url = "http://www.doviz.com/"
webData = requests.get(url)
soup = BeautifulSoup(webData.content, "html.parser")
USD = soup.find("span", {"data-socket-key": "USD", "data-socket-attr": "s"}).text
EUR = soup.find("span", {"data-socket-key": "EUR", "data-socket-attr": "s"}).text
GBP = soup.find("span", {"data-socket-key": "GBP", "data-socket-attr": "s"}).text
print(' Dolar : {}'.format(USD))
print(' Euro : {}'.format(EUR))
print(' Sterlin : {}'.format(GBP))
