# -*- coding: utf-8 -*-
import requests
import urllib.request
import json
import markdown
from datetime import datetime
import re

now = datetime.now() # current date and time
#public204381526
#club204157576
#public205281328
#public184647416
def vk():
    url = 'https://wtf.roflcopter.fr/rss-bridge/?action=display&bridge=Vk&u=public184647416&hide_reposts=on&format=Json'
    req = urllib.request.Request(url)
    date_time = now.strftime("%Y-%m-%d")
    print("date and time:",date_time)
    ##parsing response
    r = urllib.request.urlopen(req).read()
    cont = json.loads(r)
    counter = 0
    patt = "\
    --- \n\
    layout: post \n\
    --- \n\
    "
    ##parcing json
    for item in cont['items']:
        counter += 1
        print("Title:", item['author']['name'], "\Content_html:", item['content_html'])
        print("----")   
        with open("./_posts/"+date_time+"-"+str(item['_rssbridge']['post_id'])+".mdx", 'w') as f:
            f.write(patt+"\n\n"+item['content_html'])
            f.close() 
    print("Number of titles: ", counter)

def blog():
    url = 'https://wtf.roflcopter.fr/rss-bridge/?action=display&bridge=WordPress&url=https%3A%2F%2Fwww.siamcasinosonline.com%2F%25E0%25B8%259A%25E0%25B8%2597%25E0%25B8%2584%25E0%25B8%25A7%25E0%25B8%25B2%25E0%25B8%25A1%2F&format=Json'
    req = urllib.request.Request(url)
    date_time = now.strftime("%Y-%m-%d")
    print("date and time:",date_time)
    ##parsing response
    r = urllib.request.urlopen(req).read()
    cont = json.loads(r)
    counter = 0
    patt = "---\nlayout: post\n---\n"
    #print(cont)   
    ##parcing json
    for item in cont['items']:
        counter += 1
        contentA = item['content_html'].split('<div class="space-title-box-h1 relative">')
        contentX = contentA[1].split('<div class="space-page-content-tags box-100 relative">')
        reText1 = re.sub(r'(?is)<!-- Breadcrumbs Start -->.+<div class="space-page\-content\-featured-img box\-100 relative">', '', contentX[0])
        reText2 = re.sub(r'(?is)<img src.+<\/noscript>', '', reText1)
        reText3 = re.sub(r'(?is)<div class="space-page\-content\-box\-wrap relative">', '', reText2)
        reText4 = re.sub(r'(?is)<[^>]*>', '', reText3)
        print("Title:", item['title'], "\Content_html:", reText4)
        print("----")   
        with open("./_posts/"+date_time+"-"+str(counter)+".md", 'w') as f:
             f.write(patt+"\n\n"+"# "+item['title']+"\n"+reText4)
             f.close() 
    print("Number of titles: ", counter)
blog()
# https://wtf.roflcopter.fr/rss-bridge/?action=display&bridge=WordPress&url=https%3A%2F%2Fwww.siamcasinosonline.com%2F%25E0%25B8%259A%25E0%25B8%2597%25E0%25B8%2584%25E0%25B8%25A7%25E0%25B8%25B2%25E0%25B8%25A1%2F&format=Json