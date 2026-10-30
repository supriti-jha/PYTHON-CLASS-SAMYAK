# API -application programming interface
import urllib.request as url
import json
name = input("Enter Name : ").replace(" ","+")
path = f"https://api.giphy.com/v1/gifs/search?api_key=d3vBGqDiJidgq3fFmzOyjFam6iEuHxyD&q={name}&limit=25&offset=0&rating=g&lang=en&bundle=messaging_non_clips"
response  =url.urlopen(path)
# print(path)
data = json.load(response)
# print(data)
i=1
for item in data["data"]:
    url.urlretrieve(item["images"]["original"]["url"],f"{name}{i}.gif")
    i+=1 