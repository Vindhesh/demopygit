import requests
from bs4 import BeautifulSoup
request = requests.get('https://www.xe.com/currencyconverter/convert/api/page_resources/converter.php?fromCurrency=USD&toCurrency=INR')
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class":"converterresult-toAmount"})
print(element)

# <span class="converterresult-toAmount">71.7419</span>

print(request.content)

