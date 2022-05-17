import requests, re
from bs4 import BeautifulSoup

regex = r"[0-9]+(?:\.[0-9]+){3}:[0-9]+"
c = requests.get("https://spys.me/proxy.txt")
test_str = c.text
a = re.finditer(regex, test_str, re.MULTILINE)
with open("proxies_list.txt", 'w') as file:
    for i in a:
       print(i.group(),file=file)
#==========================================================

c = requests.get("https://free-proxy-list.net/")
soup = BeautifulSoup(c.content, 'html.parser')
z = soup.find('textarea').get_text()
x = re.findall(regex, z)
with open("proxies_list.txt", "a") as myfile:
    for i in x:
        print(i, file=myfile)
