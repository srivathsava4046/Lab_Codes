import requests
from bs4 import BeautifulSoup

r = requests.get("https://python-bloggers.com/")
soup = BeautifulSoup(r.content, 'html.parser')
ans = soup.prettify()
#print(ans)


with open("output.txt", "w", encoding="utf-8") as f:
    f.write("{}".format(ans))
