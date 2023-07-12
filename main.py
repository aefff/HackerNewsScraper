import requests
from bs4 import BeautifulSoup
import pprint
link = 'https://news.ycombinator.com/news'
res = requests.get(link)
soup = BeautifulSoup(res.text,'html.parser')
def nextPage(res, soup):
    nextL = soup.select('.title')
    addon = nextL[-1].a.get('href')
    link = 'https://news.ycombinator.com/news'
    link = link + addon
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')
    return res, soup
def goodThings():
    stuff = soup.select('.titleline')
    subtext = soup.select('.subtext')
    hn = []
    for index, item in enumerate(stuff):
        vote = subtext[index].select('.score')
        href = item.a.get('href', None)
        title = item.getText()
        if len(vote):
            score = int(vote[0].getText().replace(' points', ''))
            if score>100:
                hn.append({'title': title, 'link': href, 'score': score})
    return sorted(hn, key=lambda k:k['score'], reverse=True)

x=True
while x:
    print('*******************************')
    pprint.pprint(goodThings())
    res, soup = nextPage(res, soup)
    x=bool(int(input('Please enter true(1) or false(0): ')))
