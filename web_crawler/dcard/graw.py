import requests
import pandas as pd

url = 'https://www.dcard.tw/_api/posts?popular=true&limit=10'
requ = requests.get(url)
#print(requ.json())
rejs = requ.json()
f = open('output.txt', 'w')
maxwidth = 0

for item in rejs:
    if(len(item['title']) > maxwidth):
        maxwidth = len(item['title'])
print(maxwidth)
for item in rejs:
    #f.write("標題: {}, urls: {}\n".format(item['title'], 'www.dcard.tw/f/' + item['forumAlias'] + '/p/' + str(item['id'])))
    print("標題: {title:<{width}}, urls: {url}\n".format(title = item['title'],width =  maxwidth, url = 'www.dcard.tw/f/' + item['forumAlias'] + '/p/' + str(item['id'])))