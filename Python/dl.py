import os
import urllib.request
def download(url):
    filename = os.getcwd() + '\\data\\' + url.split('/')[-1]
    urllib.request.urlretrieve(url, filename=filename)
