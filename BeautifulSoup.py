import urllib2
from bs4 import BeautifulSoup

quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class':'name'})
name = name_box.text.strip()
print name

price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print price

storys = soup.find_all('div', attrs={'class':'news-story__headline'})

for story in storys:
    story_address = story.find('a', href=True)
    story_address = story_address['href']
    print story_address
    page = urllib2.urlopen(story_address)
    link_soup = BeautifulSoup(page, 'html.parser')
    author = link_soup.find('div', attrs={'class':'author'})
    print type(author)
    print author
    print '-------------------------------'
