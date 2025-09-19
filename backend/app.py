#Montar el framework (Flask)
from flask import Flask, request, jsonify
from apis import get_googleBooks, get_openLibrary
from emotions import franjas

app = Flask(__name__)

@app.route("/")
def formulario():
    return """
        <h1>Buscador de libros segun emociones<h1>
        <form action="/submit" method="post">
            <label for="texto">Escribe un texto:</label><br>
            <textarea name="texto" rows="4" cols="50" ></textarea><br><br>
            <button type="submit">Analizar</button>
        </form>
        """


@app.route("/submit", methods=['POST'])
def books():
#Procesa los datos del formulario
    texto = request.form.get("texto") #Se recoge el texto del usuario
    emocion = franjas(texto)
    libros_gb = get_googleBooks(emocion, maxResults=3)
    libros_ol = get_openLibrary(emocion, maxResults=3)
    
    return jsonify({
        "texto": texto,
        "emocion_detectada": emocion,
        "gb_books": libros_gb,
        "ol_books": libros_ol
    })

if __name__ == '__main__':
    app.run(debug=True)     #Ejecuta la app en modo debug