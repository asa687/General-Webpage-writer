""" 
this is a simple page scraper that retrieves a webpage and stores it into a .txt file


"""

import re
from urllib.request import urlopen   
print("enter the desired url: ")
url = input() 
webpage = urlopen(url) 
## the decodes for page are more complex due to certain characters being unavailable in uft-8
page = (webpage.read()).decode("utf-8").encode('cp850','replace').decode('cp850') 
pattern = "<title.*?>.*?</title.*?>"
if (re.search(pattern,page, re.IGNORECASE) != None): 
    titles = re.search(pattern,page, re.IGNORECASE) 
    title = titles.group() 
    title = re.sub("<.*?>", "", title)
else: 
    title = url
webpageFile = open(title + ".txt", 'a')  
page = re.sub("<.*?>", "", page)
webpageFile.write(page) 
webpageFile.close()



