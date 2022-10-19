import requests
URL = "https://the-dune-api.herokuapp.com/books/3"

name = input("> ")

response = requests.get (URL + f"?title={name}")
out = response.json()

print("\n",out,"\n")