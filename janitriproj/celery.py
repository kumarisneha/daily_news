from __future__ import absolute_import
import os
import re
import requests
import unicodedata
from django.conf import settings
from celery import Celery
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from bs4 import BeautifulSoup
from django.db import IntegrityError



# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'janitriproj.settings')
app = Celery('janitriproj')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

def fetchurl(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    else:
        return False

def parsedoc(html_doc):
    s=BeautifulSoup(html_doc,"html.parser")
    return s.find_all("div", class_="news-card z-depth-1")

def main():
    from janitriapp.models import UserInterest, NewsWebsite
    list_interest = ["entertainment", "sports", "technology"]
    i=1
    for interest in list_interest:    
        s = "https://www.inshorts.com/en/read/%s" % interest
        html_doc = fetchurl(s)
        if html_doc:
            result = parsedoc(html_doc)
        for a in range(len(result)):
            style=result[a].find('div')['style']
            urls = re.findall('url\((.*?)\)', style)
            y=result[a].find_all("a",class_="clickable")
            desc = result[a].find_all("div",class_="news-card-content news-right-box")        
            try:
                description = str(desc[0].div.text)
                title = str(y[0].span.text)
                image = str(urls[0]).strip("'")
                try:
                    a = NewsWebsite(title = title, url = image, description= description, interest = i)
                    a.save()
                except IntegrityError as e:
                    pass
                print title
                print image
                print "----------------------------------------------------------------------------"
                print description
            except UnicodeEncodeError as e:
                continue
                # print unicodedata.normalize('NFKD', (desc[0].div.text).encode('ascii', 'ignore'))
            print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        i = i+1
        
@periodic_task(run_every=(crontab(minute='*/30')), name="some_task", ignore_result=True)
def some_task():
    main()
