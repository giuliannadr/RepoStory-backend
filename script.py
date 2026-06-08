import requests

respuesta = requests.get("https://api.github.com/users/giuliannadr")
print("Nombre:", respuesta.json()["name"])
print("Repos Publicos:", respuesta.json()["public_repos"])
print("Ubicacion:", respuesta.json()["location"])