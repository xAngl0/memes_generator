# Importar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Resultados del formulario
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # obtener la imagen seleccionada
        selected_image = request.form.get('image-selector')

        # Asignación #2. Recepción del texto
        textTop=request.form.get("textTop")
        textBottom= request.form.get("textBottom")

        # Asignación #3. Recepción del color
        color= request.form.get("color-selector")

        # Asignación #4. Recepción del posicionamiento del texto
        textTop_y=request.form.get("textTop_y")
        textBottom_y=request.form.get("textBottom_y")

        return render_template('index.html', 
                               # Visualización de la imagen seleccionada
                               selected_image=selected_image, 

                               # Asignación #2. Visualización del texto
                               textTop=textBottom,
                               textBottom=textBottom,
                               
                               #  Asignación #3. Visualización del color
                               color_selector=color,
                               
                               # Asignación #4. Visualización de la posición del texto
                               textTop_y=textBottom_y, 
                               textBottom_y=textBottom_y

                               )
    else:
        # Mostrar la primera imagen por defecto
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
