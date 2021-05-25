import requests,bs4,sys,webbrowser

inp = input('What do you want to search: ')
res = requests.get('https://google.com/search?q='+''.join(inp))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
linkElements = soup.select('.kCrYT > a')

linkToOpen = min(5, len(linkElements))
for i in range(linkToOpen):
    webbrowser.open('https://google.com'+linkElements[i].get('href'))
