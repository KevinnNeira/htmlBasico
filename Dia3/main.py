from tabulate import tabulate
import requests

datos = requests.get("http://localhost:5505")
datos = datos.json()
print(tabulate(datos, headers="keys", tablefmt="html"))