import requests
# # request = requests.get('https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01&base=USD HTTP/1.1')
# people = requests.get('http://api.open-notify.org/astros.json')
# print(people.text)
# print(people.status_code)
# people_json = people.json()
# print(people_json)

# #To print the number of people in space
# print("Number of people in Space: ", people_json['number'])

# #To print the names of people in space using a for loop
# for p in people_json['people']:
#     print(p['name'])

# for p in people_json['people']:
#     print(p['craft'])

parameter = {"rel_rhy":"jingle"}
request = requests.get('https://api.datamuse.com/words', parameter)
# print(request.text)
rhyme_json = request.json()
# print(request_json)
for i in rhyme_json[:]:
    print(i['word'])