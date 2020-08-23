import bs4 as bs
import urllib.request

link = input("Paste your URL: \n")

source = urllib.request.urlopen(link).read()

soup = bs.BeautifulSoup(source, 'lxml')

print(soup.text)