import urllib2
from sgmllib import SGMLParser

class WeatherList(SGMLParser):
    is_td = ""
    name = []
    def start_td(self, attrs):
        self.is_td = 1
    def end_td(self):
        self.is_td = ""
    def handle_data(self, text):
       if self.is_td:
           self.name.append(text)

content = urllib2.urlopen('http://www.cwb.gov.tw/V7/forecast/taiwan/Taipei_City.htm').read()

Temperature = WeatherList()
Temperature.feed(content)

for i in Temperature.name:
    if '\t' not in i:
        print i.decode('utf-8')
