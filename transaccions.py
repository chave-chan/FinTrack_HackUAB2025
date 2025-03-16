#FUNCIONA LA IA DE LA MASCOTAAAAA /FILTRADO POR PAIS
import requests
import json

# Definir la clave de API de Perplexity
API_KEY = "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"  # Reemplaza con tu clave de Perplexity

# URL de la API de Perplexity (verifica la URL correcta)
url = "https://api.perplexity.ai/chat/completions"  # Asegúrate de que esta URL sea correcta

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Leer y validar los datos JSON GASTOS 
with open("gastos.json", "r", encoding="utf-8") as archivo:
    gastos_json = json.load(archivo)

# Convertir los gastos a una cadena de texto
gastos_str = ", ".join(f"{gasto['Título']} ({gasto['Categoría']}): ${gasto['Monto']}" for gasto in gastos_json)

# Leer y validar los datos JSON ORIGEN 
with open("origen.json", "r", encoding="utf-8") as archivo:
    origen_json = json.load(archivo)

# Convertir los gastos a una cadena de texto
origen_str = ", ".join(f"{origen['Pais']}" for origen in origen_json)

# Crear los mensajes para la solicitud
messages = [
    {
        "role": "system",
        "content": "Eres un asistente financiero llamado Finn. Analiza los gastos y da consejos de ahorro. Presentate primero. No preguntes nada. Ten en cuenta el país de origen al dar consejos"
    },
    {
        "role": "user",
        "content": f"Gastos del mes: {gastos_str},{origen_str}"
    }
]

# Crear el cuerpo de la solicitud
data = {
    "model": "sonar-pro",  # Asegúrate de que este modelo sea el adecuado
    "messages": messages
}

try:
    # Hacer la solicitud a la API
    response = requests.post(url, json=data, headers=headers)

    # Imprimir el código de respuesta y el contenido
    print(f"Código de respuesta: {response.status_code}")
    print("Contenido de la respuesta:", response.text)  # Imprimir el cuerpo de la respuesta

    if response.status_code == 200:
        result = response.json()
        print("Análisis Financiero:")
        print(result['choices'][0]['message']['content'])  # Acceder al contenido de la respuesta
    else:
        print("Error al llamar a la API:", response.status_code)
        print(response.json())

except requests.exceptions.RequestException as e:
    print("Ha ocurrido un error, por el momento no puedo ayudarte. Inténtalo más tarde", e)
except Exception as e:
    print("Por el momento no tengo consejos financieros para ti", e)
