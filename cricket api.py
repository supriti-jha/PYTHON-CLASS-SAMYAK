import urllib.request as url
import json
name = input("Enter Cricketer name : ")
path = f"https://api.cricapi.com/v1/players?apikey=56c49b31-39fb-4d71-8de7-8ef05a480640&offset=0&search={name}"
response = url.urlopen(path)
data = json.load(response)
id = data["data"][0]["id"]

path = f"https://api.cricapi.com/v1/players_info?apikey=56c49b31-39fb-4d71-8de7-8ef05a480640&id={id}"
response = url.urlopen(path)
data = json.load(response)

data = data["data"]
print("Name : ",data["name"])
print("Role : ",data["role"])
print("Batting Style : ",data["battingStyle"])
print("Country : ",data["country"])

url.urlretrieve(data["playerImg"],name+".png")