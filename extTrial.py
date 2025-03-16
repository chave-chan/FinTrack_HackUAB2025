from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def check_rating(page_url):
    headers = {"User-Agent": "Mozilla/5.0"}  # Mimic a browser
    response = requests.get(page_url, headers=headers)
    
    if response.status_code != 200:
        return "No puedo analizar la seguridad de tu página. Es mejor no arriesgarse!"  # Si la página no responde correctamente, devolver "No"
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Buscar el texto de la calificación
    rating_tag = soup.find('h4', class_='typography_heading-xxs__UmE9o typography_appearance-default__t8iAq styles_starRatingName__Zw715')

    try:
        if rating_tag:
            rating_text = rating_tag.get_text(strip=True)  # Extraer el texto correctamente
            #print(f"Rating encontrado: {rating_text}")  # Verificar el texto extraído

            if rating_text in ["Bad", "Poor"]:
                return "No te recomiendo seguir, está página no es segura"
            elif rating_text in ["Average", "Great", "Excellent"]:
                return "No te preocupes, la página que visitas es segura"
        else:
            print("No se encontró la calificación.")
            return "No seguro"
        
    except Exception as e:
        print("No puedo analizar la seguridad de tu página. Es mejor no arriesgarse!",e)

# Ejemplo de uso:
base_url = "https://www.trustpilot.com/review/mercadolibree.com.pe"
result = check_rating(base_url)
print(result)

#definimos la ruta

@app.route('/check', methods=['POST']) #POST porque enviamos datos al servidor
def check_reputation():
    data = request.get_json()  # Obtener los datos JSON enviados por la extensión
    url = data['url']  # Obtener la URL de la solicitud

    result = check_rating(url)  # Analizar la URL usando la función definida

    return jsonify({'result': result})  # Devolver el resultado como JSON

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

