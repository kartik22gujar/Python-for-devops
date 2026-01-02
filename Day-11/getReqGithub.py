import requests

url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'
response = requests.get(url)

pull_req = response.json()

for i in pull_req:
    cret = i['user']['login']
    print(cret)