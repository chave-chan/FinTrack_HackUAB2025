#QUERY
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

# Crear el cuerpo de la solicitud
def obtener_respuesta(query_str):
    # Crear los mensajes para la solicitud
    messages = [
        {
            "role": "system",
            "content": "Eres un asistente financiero llamado Finn. Analiza los gastos y da consejos de ahorro. Presentate primero."
        },
        {
            "role": "user",
            "content": f"Gastos del mes: {query_str}"
        }
    ]

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

# Interacción continua con el usuario
while True:
    # Solicitar la consulta al usuario
    query_input = input("Ingresa tu consulta o escribe 'salir' para terminar: ")

    # Salir del programa si el usuario escribe 'salir'
    if query_input.lower() == 'salir':
        print("Gracias por usar el asistente financiero. ¡Hasta luego!")
        break

    # Crear el query a partir de la entrada del usuario
    query_str = f"Consulta: {query_input}"

    # Llamar a la función para obtener la respuesta del bot
    obtener_respuesta(query_str)
