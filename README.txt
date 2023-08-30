Pasos para Ejecutar la API de Entidades Nombradas con Pythony Flask

0. Descarga de repositorio:
    a) Descargar utilizando comandos de git
        - git clone https://github.com/eerubio/entity_recognition_app.git
    b) Descargar el repositorio directo de la siguiente página
        - https://github.com/eerubio/entity_recognition_app.git

1. Instalación de Dependencias:
   a) Tener Python y pip instalados en el sistema.
        - Si no los tienes, descargarlo e instalar Python desde https://www.python.org/downloads/
        - Pip debería estar incluido en la instalación.

   b) Instalar las dependencias necesarias ejecutando el siguiente comando en la terminal:
    - pip install -r requirements.txt

2. Ejecutar la API:
    a) Abrir una terminal o línea de comandos
    b) Navega al directorio donde se tiene el archivo app.py
    c) Ejecutar el siguiente comando:
        => python app.py
    d) Si se ejecutó correctamente la API apareceran los siguientes mensajes en consola
         * Running on all addresses (0.0.0.0)
         * Running on http://127.0.0.1:5000
         * Running on http://192.168.100.183:5000
    e) Por cada solicitud la consola se actualizará con un código al final que indica el estado de la solicitud
        - 200 OK: La solicitud se procesó con éxito y se devuelven los resultados.
        - 400 Bad Request: Se devuelve si no se proporcionaron oraciones en la solicitud.
        - 500 Internal Server Error: Se devuelve si ocurre un error en el servidor al procesar la solicitud.

3. Prueba la API:
    a) Puedes probar la API enviando solicitudes a través de herramientas como cURL o Postman
    b) Abriendo el archivo index.html en un navegador, el cual tendra una interfaz para mandar oraciones.
        i.g. Cuadro Oraciones => |"Apple está buscando comprar una startup del Reino Unido por mil millones de dólares."|
                                 |"San Francisco considera prohibir los robots de entrega en la acera."                 |
    c) Ejecutando comando en consola =>
        curl -X POST -H "Content-Type: application/json" -d '{"sentences":
        ["Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
         "San Francisco considera prohibir los robots de entrega en la acera."]}' http://127.0.0.1:5000/ner

4. Detener el servidor:
    a) Detener el servidor presionando Ctrl + C en la terminal donde se está ejecutando el servidor de Flask.




