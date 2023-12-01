from flask import Flask, render_template, send_file
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/descargar_pdf')
def descargar_pdf():
    nombre_archivo = "archivo.pdf"
    crear_pdf(nombre_archivo)
    return send_file(nombre_archivo, as_attachment=True)
