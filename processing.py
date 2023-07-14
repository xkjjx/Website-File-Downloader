import sys
import urllib.request as r
from urllib.parse import urlparse
import os

def getExtension(s):
    return s.split(".")[-1]

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def getParentDirectoryUrl(url):
    parsedUrl = urlparse(url)
    return parsedUrl._replace(path='/'.join(parsedUrl.path.split('/')[:-1])).geturl()

def getFileName(i,text,extension):
    if(text[i - len(extension) - 1: i] == bytes("." + extension,"utf-8")):
        temp = extension
        j = len(extension) + 1
        while (text[i - j] != 34):
            temp = chr(text[i - j]) + temp
            j += 1
        return temp
    return ""
def getFileNames(fileLinks,url,extensions):
    page = r.urlopen(r.Request(url,headers=hdr))
    text = page.read()
    for i in range(5,len(text)):
        for extension in extensions:
            fName = getFileName(i,text,extension)
            if fName != "":
                fileLinks.append(fName)

def downloadFiles(url,links,folder,indexNaming):
    success = []
    failures = []
    i = 0
    folderPath = os.path.join(os.path.expanduser("~"),"Downloads",folder)
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)
    for link in links:
        pageURL = link.replace(" ", "_")
        if indexNaming:
            fName = os.path.join(folderPath,str(i) + "." + getExtension(pageURL))
        else:
            fName = os.path.join(folderPath,link.replace("-", " ").replace("/","_"))
        print(fName)
        try:
            if indexNaming:
                r.urlretrieve(pageURL, filename = fName)
            else:
                r.urlretrieve(link, filename = fName)
            success.append(pageURL)
        except:
            try:
                if indexNaming:
                    r.urlretrieve(getParentDirectoryUrl(url) + "/" + pageURL, filename = fName)
                else:
                    r.urlretrieve(getParentDirectoryUrl(url) + "/" + pageURL, filename = fName)
                success.append(getParentDirectoryUrl(url) + "/" + pageURL)
            except:
                print(sys.exc_info())
                print(folder,folder + "/" + link.replace("-", " ").replace(".", " "))
                print(pageURL)
                failures.append(pageURL)
                continue
        i += 1
    return success,failures


def full(url,extensions,folderName,indexNaming):
    fileLinks = []
    getFileNames(fileLinks,url,extensions)
    return downloadFiles(url,fileLinks,folderName,indexNaming)





