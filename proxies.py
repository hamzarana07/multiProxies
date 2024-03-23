import requests, re
from bs4 import BeautifulSoup

regex = r"[0-9]+(?:\.[0-9]+){3}:[0-9]+"
c = requests.get("https://spys.me/proxy.txt")
test_str = c.text
a = re.finditer(regex, test_str, re.MULTILINE)
with open("proxies_list.txt", 'w') as file:
    for i in a:
       print(i.group(),file=file)
        
d = requests.get("https://free-proxy-list.net/")
soup = BeautifulSoup(d.content, 'html.parser')
td_elements = soup.select('.fpl-list .table tbody tr td')
ips = []
ports = []
for j in range(0, len(td_elements), 8):
    ips.append(td_elements[j].text.strip())
    ports.append(td_elements[j + 1].text.strip())
with open("proxies_list.txt", "a") as myfile:
    for ip, port in zip(ips, ports):
        proxy = f"{ip}:{port}"
        print(proxy, file=myfile)
