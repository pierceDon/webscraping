from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://cfbstats.com/2024/team/51/index.html'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

tr = soup.findAll("tr")

for row in tr[1:]:
    td = soup.findAll("td")

