from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar Flask-CORS para manejar CORS
import spacy

app = Flask(__name__)
# Inicialización de Flask CORS para permitir solicitudes de diferentes orígenes
CORS(app)

# Cargar el modelo en español de SpaCy para procesar las oraciones
nlp = spacy.load("es_core_news_sm")

# La
@app.route('/ner', methods=['POST'])
def extract_entities():
    """
        Endpoint de la API que recibe una lista de oraciones y devuelve las entidades nombradas identificadas en
        cada oración.

        Método: POST
        Ruta: /ner

        Parámetros de entrada:
        - sentences (list): Una lista de oraciones en español.

        Respuesta:
        - results (list): Una lista de objetos que contienen las oraciones y sus entidades nombradas identificadas.

        Códigos de respuesta HTTP:
        - 200 OK: La solicitud se procesó con éxito y se devuelven los resultados.
        - 400 Bad Request: Se devuelve si no se proporcionaron oraciones en la solicitud.
        - 500 Internal Server Error: Se devuelve si ocurre un error en el servidor al procesar la solicitud.
    """
    try:
        data = request.get_json()
        sentences = data.get('sentences', [])

        if not sentences:
            return jsonify({'error': 'No se proporcionaron oraciones'}), 400

        results = []
        # Se recorren todas las oraciones agregadas a la lista enviada por el formato JSON
        for sentence in sentences:
            doc = nlp(sentence)
            entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
            results.append({'sentence': sentence, 'entities': entities})

        # Retorna 200 cuando la socilitud fue recibida correctamente por la API
        return jsonify({'results': results}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Retorna valor 500 cuando la solicitud falló

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Permite el acceso a la API desde cualquier computo en la misma red