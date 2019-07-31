from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import time
import re
import csv

fields = ['Heading', 'Content']
out_file = open('times_of_india.csv','w')
csvwriter = csv.DictWriter(out_file, delimiter=',', fieldnames=fields)
dict_service = {}

dict_service['Heading'] = "Heading"
dict_service['Content'] = "Content"

with open('data2.csv', 'a') as csvfile:
    filewriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fields)
    filewriter.writerow(dict_service)
csvfile.close()

for i in range(0,96):
    url="https://timesofindia.indiatimes.com/blogs/politics/page/"+str(i)
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    page = urllib.request.urlopen( req )
    #page=urllib2.urlopen(url)

    soup = BeautifulSoup(page.read(), "html.parser")
    services = soup.find_all('div', {'class': 'feeds'})
    services = services[0].find_all('div', {'class': 'media article'})
    
    for service in services:
        try:
            heading = service.find_all('h2', {'class': 'media-heading'})
            link = re.findall(r'(http.*?)"', str(heading))
            print(link[0])
            url_2 =str(link[0])
            req_2 = urllib.request.Request(url_2, headers={'User-Agent' : "Magic Browser"}) 
            page_2 = urllib.request.urlopen( req_2 )
            #page=urllib2.urlopen(url)
            soup_2 = BeautifulSoup(page_2.read(), "html.parser")
            heading_2 = soup_2.find_all('h1', {'class': 'media-heading h2'})
            content_2 = soup_2.find_all('div', {'class': 'content'})
            heading_2 = heading_2[0].text.encode('unicode-escape').decode('utf-8')
            content_2 = content_2[0].text.encode('unicode-escape').decode('utf-8')
            print(heading_2)
            print("------------------------------------"+str(i)+"-----------------------------------------------")
            print(content_2)
            dict_service = {}
            dict_service['Heading'] = str(heading_2)
            dict_service['Content'] = str(content_2)

            with open('data2.csv', 'a') as csvfile:
                filewriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fields)
                filewriter.writerow(dict_service)
            csvfile.close()
        except:
            print('-------------------------------------- Bhau Error --------------------------------------------------------')


        
