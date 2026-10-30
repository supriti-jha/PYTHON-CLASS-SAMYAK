import urllib.request as url
import json
path ="https://newsdata.io/api/1/latest?apikey=pub_65cc402e58b045f98651b8813db0edd3"
response=url.urlopen(path)
data = json.load(response)
result = data["results"]
x=1
for item in result:
    print(x,"=>",item["title"],end="\n\n\n\n")
    x+=1
    fdae6e79de5af9ac4aa66b522872dd0c