import requests
url = "https://opentdb.com/api.php"

parameter = {
    "amount" : 10,
    "type" : "boolean"
}

response = requests.get(url=url,params=parameter)

data = response.json()["results"]

data = data