import requests

url = "https://jsonplaceholder.typicode.com/albums/1/photos"

# enviar solicitud GET
response = requests.get(url)

# comprobar el estado de la respuesta
if response.status_code == 200:
    # La solicitud fue exitosa
    print("respuesta exitosa")
    print("contenido de la respuesta:")
    # print(response.json())  # Contenido de la respuesta

else:
    # La solicitud no fue exitosa
    print("Error en la solicitud. Codigo de estado:", response.status_code)
