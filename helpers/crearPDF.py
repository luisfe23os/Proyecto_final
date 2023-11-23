import os
import aspose.pdf as ap

def read_html_file(file_path):
    """
    Lee el contenido de un archivo HTML.

    Parameters:
    - file_path (str): Ruta del archivo HTML.

    Returns:
    - str: Contenido del archivo HTML.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def crear_pdf(html_path, output_path="output.pdf"):
    """
    Crea un archivo PDF a partir de un archivo HTML que representa una tabla u otro contenido.

    Parameters:
    - html_path (str): Ruta del archivo HTML.
    - output_path (str): Ruta de salida del archivo PDF. Por defecto, es "output.pdf".
    """
    # Verificar si el archivo HTML existe
    if not os.path.isfile(html_path):
        print(f"Error: El archivo HTML '{html_path}' no existe.")
        return

    # Inicializar objeto de documento
    document = ap.Document()

    # Añadir página
    page = document.pages.add()

    # Leer el contenido HTML desde el archivo
    html_code = read_html_file(html_path)

    # Inicializar objeto fragmento de HTML
    html_fragment = ap.HtmlFragment(html_code)

    # Agregar fragmento HTML a la nueva página
    page.paragraphs.add(html_fragment)

    # Guardar PDF actualizado
    document.save(output_path)
    print(f"El PDF ha sido creado en: {output_path}")
