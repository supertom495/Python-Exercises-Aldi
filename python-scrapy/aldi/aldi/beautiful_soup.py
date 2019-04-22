from bs4 import BeautifulSoup
soup = BeautifulSoup(open("nav.html","r+"), "lxml")
# print(open("nav.html","r+"))
# print(soup.find_all('li'))

filename = 'li'
with open(filename, 'w+') as f:
    for x in soup.find_all('li'):
        f.write(str(x))
