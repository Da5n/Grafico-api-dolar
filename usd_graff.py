import requests
import matplotlib.pyplot as plt

#Se invoca la API se procesa la respuesta como JSON
api_url = "https://mindicador.cl/api/dolar"
datos = requests.get(api_url).json()

#Se extrae el valor y la fecha del dolar 
valor_dolar = []
fecha = []
for i in range (5):
    valor_dolar_extraido = datos['serie'][i]['valor']
    valor_dolar.append(valor_dolar_extraido)
    fecha_extraccion = datos['serie'][i]['fecha']
    fecha.append(fecha_extraccion)

#Creacion del grafico 
#Asignamos los valores para cada eje mas la forma del marcador
plt.plot(fecha, valor_dolar, marker="o")
plt.title("Valor del dolar en los ultimos 5 dias")#Titulo
plt.xlabel('Fecha') #Label que da nombre al eje X
plt.ylabel('Valor del Dolar') #Label que da nombre al eje Y
#Se muestr el grafico
plt.show()