import urllib.request
import random

url = 'http://www.whatismyip.com.tw'
iplist = ['115.32.41.100:80','58.30.231.36:80','123.56.90.175:3128']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Test_Proxy_Python3.5_maminyao')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
